# TrustLayer AI

TrustLayer is an AI-powered content moderation API built with FastAPI.

It analyzes user-generated text and assigns a toxicity probability and trust score, helping platforms detect harmful or abusive language in real time.

The project demonstrates how transformer-based models can be integrated into backend systems for moderation, trust scoring, and community safety.

## Features

- FastAPI backend
- Transformer-based toxicity detection
- Trust score calculation (0–100)
- JSON API responses
- Easily extendable moderation pipeline

## How It Works

1. User submits text
2. The API sends the text to a toxicity classification model
3. The model returns probability scores
4. The system converts this into a trust score

Example logic:

trust_score = (1 - toxicity_probability) * 100

Higher trust score → safer content.

## Example Request

POST /analyze

Query parameter:

text=You are dumb

## Example Response

{
  "text": "You are dumb",
  "label": "toxic",
  "toxicity_probability": 0.977,
  "trust_score": 2
}

## Run Locally

Clone the repository

git clone https://github.com/Brahmendra-Ramoju/TrustLayer_AI.git

Enter the project directory

cd TrustLayer_AI

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn main:app --reload

Open API documentation

http://127.0.0.1:8000/docs

## Project Structure

TrustLayer_AI
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## Potential Use Cases

- Chat moderation
- Social media content filtering
- Online community safety tools
- Comment toxicity detection
- Trust scoring systems for platforms

## Future Improvements

- Spam detection
- Misinformation classification
- User reputation scoring
- Web moderation dashboard
- Deployment as a public moderation API

## Tech Stack

- Python
- FastAPI
- Transformers
- PyTorch
- Git / GitHub

## Author

Surya Sai Brahmendra Ramoju

GitHub:
https://github.com/Brahmendra-Ramoju
