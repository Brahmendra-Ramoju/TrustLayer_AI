from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TrustLayer AI Moderation API"}

@app.post("/analyze")
def analyze_text(text: str):
    if "dumb" in text.lower() or "stupid" in text.lower():
        result = "toxic"
    else:
        result = "safe"

    return {
        "text": text,
        "analysis": result
    }