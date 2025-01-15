from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat

# Inicializando o FastAPI
app = FastAPI(
    title="Chatbot Especialista em Cinema 🎬🤖",
    description="Responde perguntas sobre filmes usando TMDb e LLM.",
    version="1.0.0",
)

# Configuração do CORS (se for necessário para o front-end)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat", tags=["Chatbot"])

@app.get("/")
async def root():
    return {"message": "Chatbot de Cinema está funcionando! 🎬"}
