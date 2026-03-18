# backend/main.py

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from model_loader import predict
from chatbot_handler import chatbot_start, chatbot_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_stage = None

@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    global current_stage

    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    stage = predict(image)
    current_stage = stage

    chatbot_intro = chatbot_start(stage)

    return {
        "stage": stage,
        "chatbot": chatbot_intro
    }


@app.post("/chat/")
async def chat(user_message: str):
    global current_stage

    reply = chatbot_reply(current_stage, user_message)

    return {
        "reply": reply
    }