import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import HTTPException

# .env dosyasını yükle
load_dotenv()

# API anahtarını al
api_key = os.getenv("GEMINI_API_KEY")

# Gemini API'sini yapılandır
genai.configure(api_key=api_key)


def generate_feedback(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        # Eğer response başarılıysa sadece metin döndür
        if response:
            return response.text
        else:
            raise HTTPException(status_code=500, detail="No content received from Gemini API.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interacting with Gemini API: {str(e)}")
