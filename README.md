# TrustLayer API

TrustLayer is a lightweight content moderation API built with FastAPI.

It analyzes user text and classifies it as safe or toxic. The project demonstrates how to build a simple moderation layer that could be integrated into social platforms, chat systems, or community applications.

## Features

- FastAPI backend
- Simple toxicity detection
- JSON API response
- Easy to extend with AI moderation models

## Example Request

POST /analyze

Query:

text=You are dumb

Response:

{
  "text": "You are dumb",
  "analysis": "toxic"
}

## Run Locally

1. Clone the repository

git clone https://github.com/Brahmendra-Ramoju/TrustLayer_AI.git

2. Enter the project

cd TrustLayer_AI

3. Install dependencies

pip install fastapi uvicorn

4. Run the server

uvicorn main:app --reload

5. Open API docs

http://127.0.0.1:8000/docs

## Future Improvements

- AI-based toxicity detection
- Trust scoring
- User reputation system
- Deployment as a hosted API

## Example

POST /analyze

Input:
You are dumb

Response:

{
  "text": "You are dumb",
  "label": "toxic",
  "toxicity_probability": 0.977,
  "trust_score": 2
}
