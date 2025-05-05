import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_feedback(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text