from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env faylni yuklash

app = FastAPI()

API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
URL = "https://translation.googleapis.com/language/translate/v2"

class TranslateRequest(BaseModel):
    text: str
    target_language: str

@app.post("/translate/")
async def translate_text(request: TranslateRequest):
    """Matnni tarjima qiluvchi API"""
    params = {
        "q": request.text,
        "target": request.target_language,
        "key": API_KEY
    }
    response = requests.post(URL, data=params)
    if response.status_code == 200:
        translated_text = response.json()["data"]["translations"][0]["translatedText"]
        return {"translated_text": translated_text}
    return {"error": "Tarjima qilishda xatolik yuz berdi"}
