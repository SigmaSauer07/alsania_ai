from fastapi import APIRouter
from app.ipfs_handler import fetch_latest_dataset
from app.ai_model import process_message

router = APIRouter()

@router.get("/dataset")
def get_dataset():
    return fetch_latest_dataset()

@router.post("/chat")
def chat(input_text: str):
    return process_message(input_text)
