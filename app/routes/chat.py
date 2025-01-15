from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm import generate_response
from app.utils.guardrails import apply_guardrails

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


# TODO: Implementação aqui da escolha de outros modelos


@router.post("/ask")
def ask_chatbot(request: QuestionRequest):
    question = request.question
    print(f"Recebendo a pergunta do usuário: {question}")

    if not question.strip():
        raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")

    try:
        print("Processando a pergunta com o agente LangChain.")
        response = generate_response(question)

        print(f"Resposta final após aplicação das regras: {apply_guardrails(response)}")
        return {apply_guardrails(response)}

    except Exception as e:
        print(f"Erro durante o processamento da pergunta: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Ocorreu um erro ao processar sua pergunta: {str(e)}",
        )
