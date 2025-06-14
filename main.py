import streamlit as st
from firecrawl_scraper import scrape_with_bs4
from gemini_writer import ai_spin_chapter, ai_review_chapter
from chroma_store import store_version, get_versions

st.title("📚 Automated Book Publication Workflow")

url = st.text_input("Enter Chapter URL to Scrape:", value="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")
chapter_id = st.text_input("Chapter ID:", value="chapter_1")

if st.button("Scrape Chapter"):
    with st.spinner("Scraping..."):
        original = scrape_with_bs4(url)
        st.session_state["original"] = original
        st.text_area("Original Chapter Text", original, height=300)

if "original" in st.session_state:
    if st.button("AI Spin Chapter"):
        with st.spinner("Rewriting with Gemini..."):
            spun = ai_spin_chapter(st.session_state["original"])
            st.session_state["spun"] = spun
            store_version(spun, "ai_writer", chapter_id)
            st.text_area("AI-Spun Version", spun, height=300)

    if "spun" in st.session_state:
        edited = st.text_area("Human Edit Area", st.session_state["spun"], height=300)
        if st.button("Finalize"):
            store_version(edited, "final", chapter_id)
            st.success("Final version stored successfully!")

if st.button("Show All Versions"):
    versions = get_versions(chapter_id)
    for doc, meta in zip(versions['documents'], versions['metadatas']):
        st.subheader(f"{meta['version'].capitalize()} Version")
        st.text_area("", doc, height=200)
