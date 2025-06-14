import google.generativeai as genai

genai.configure(api_key="AIzaSyAz2txMaT-bDKD7_rYx6DBnCwrJ_B1f5R4")
model = genai.GenerativeModel("gemini-2.0-flash")

def ai_spin_chapter(content, prompt="Rewrite this chapter with better clarity and flow."):
    response = model.generate_content(f"{prompt}\n\n{content}")
    return response.text.strip()

def ai_review_chapter(content):
    review_prompt = "Review and refine this content for grammar, clarity, and coherence."
    return ai_spin_chapter(content, review_prompt)
