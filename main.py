from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load AI moderation model
classifier = pipeline(
    "text-classification",
    model="unitary/toxic-bert",
    top_k=None
)

@app.get("/")
def home():
    return {"message": "TrustLayer AI Moderation API"}

@app.post("/analyze")
def analyze_text(text: str):

    result = classifier(text)[0]

    toxicity = result["score"]
    label = result["label"]

    trust_score = round((1 - toxicity) * 100)

    return {
        "text": text,
        "label": label,
        "toxicity_probability": round(toxicity, 3),
        "trust_score": trust_score
    }