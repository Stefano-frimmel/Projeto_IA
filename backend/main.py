from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import torch

app = FastAPI()

# Permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar modelo de linguagem (modelo público via Hugging Face)
# Usando Falcon 7B Instruct, que é open-source e não exige autenticação
chatbot = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", torch_dtype=torch.float16, device_map="auto")

class Message(BaseModel):
    question: str

@app.post("/chat")
async def chat(msg: Message):
    response = chatbot(msg.question, max_new_tokens=128, do_sample=True, temperature=0.7)
    answer = response[0]["generated_text"][len(msg.question):].strip()
    return {"answer": answer}
