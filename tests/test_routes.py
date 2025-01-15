from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_movie():
    response = client.get("/movies/search?movie_name=Deadpool")
    assert response.status_code == 200
    assert response.json() is not None
    assert "results" in response.json()  # Exemplo de chave esperada na resposta

def test_popular_movies():
    response = client.get("/movies/popular")
    assert response.status_code == 200
    assert response.json() is not None
    assert "results" in response.json()  # Exemplo de chave esperada na resposta

def test_top_rated_movies():
    response = client.get("/movies/top_rated")
    assert response.status_code == 200
    assert response.json() is not None
    assert "results" in response.json()  # Exemplo de chave esperada na resposta

def test_movie_details():
    response = client.get("/movies/567604")
    assert response.status_code == 200
    assert response.json() is not None
    assert "title" in response.json()  # Exemplo de chave esperada no detalhe do filme

def test_movie_question(self, mock_generate_response):
    # Definindo o mock para a resposta gerada
    mock_generate_response.return_value = "O ator principal de Deadpool é Ryan Reynolds."
        
    # Fazendo a pergunta ao chatbot
    response = client.post("/ask", json={"question": "Qual é o ator principal de Deadpool?"})
        
    # Verificando se a resposta foi correta
    assert response.status_code == 200
    assert response.json() == {"response": "O ator principal de Deadpool é Ryan Reynolds."}

def test_non_movie_question(self, mock_generate_response):
        # Definindo o mock para a resposta gerada
        mock_generate_response.return_value = "Programação é uma habilidade muito importante no mundo da tecnologia."

        # Fazendo a pergunta fora do contexto de filmes
        response = client.post("/ask", json={"question": "Você sabe algo sobre programação?"})

        # Verificando se a resposta foi filtrada corretamente
        assert response.status_code == 200
        assert response.json() == {"response": "Desculpe, mas isso não está relacionado a filmes. Pergunte-me sobre filmes, atores ou diretores!"}
        