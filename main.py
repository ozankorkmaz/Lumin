from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Kullanıcı giriş verilerini temsil eden model
class UserInput(BaseModel):
    age: int
    skin_type: str
    mood: str
    fragrance_preference: str
    lifestyle: str

# Örnek parfüm listesi
perfume_db = {
    "Floral": ["Dior J'adore", "Chanel No.5", "Gucci Bloom"],
    "Woody": ["Tom Ford Oud Wood", "Creed Aventus", "Le Labo Santal 33"],
    "Citrus": ["Acqua di Gio", "Dolce & Gabbana Light Blue", "Chanel Allure Homme Sport"],
    "Spicy": ["YSL La Nuit De L'Homme", "Versace Eros", "Paco Rabanne One Million"]
}

@app.post("/recommend")
def recommend_perfume(user: UserInput):
    fragrance = user.fragrance_preference
    recommendations = perfume_db.get(fragrance, ["No match found"])
    return {"recommended_perfume": random.choice(recommendations)}
