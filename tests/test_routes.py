from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Esses são testes unitários utilizados no início da criação desse projeto
# Então para a construção desse projeto, foi utilizada a filosofia de primeiro tentar
# fazer os testes, para depois iniciar o código, ou seja, em um formato já imaginando
# os resultados esperados, antes mesmo de ter o código

def test_search_movie():
    response = client.get("/movies/search?movie_name=Deadpool")
    assert response.status_code == 200
    assert response.json() is not None
    assert "results" in response.json()

def test_popular_movies():
    response = client.get("/movies/popular")
    assert response.status_code == 200
    assert response.json() is not None
    assert "results" in response.json()

def test_top_rated_movies():
    response = client.get("/movies/top_rated")
    assert response.status_code == 200
    assert response.json() is not None
    assert "results" in response.json() 

def test_movie_details():
    response = client.get("/movies/567604")
    assert response.status_code == 200
    assert response.json() is not None
    assert "title" in response.json()

def test_movie_question(self, mock_generate_response):
    mock_generate_response.return_value = "O ator principal de Deadpool é Ryan Reynolds."
        
    response = client.post("/ask", json={"question": "Qual é o ator principal de Deadpool?"})
        
    assert response.status_code == 200
    assert response.json() == {"response": "O ator principal de Deadpool é Ryan Reynolds."}

def test_non_movie_question(self, mock_generate_response):
        mock_generate_response.return_value = "Programação é uma habilidade muito importante no mundo da tecnologia."

        response = client.post("/ask", json={"question": "Você sabe algo sobre programação?"})

        assert response.status_code == 200
        assert response.json() == {"response": "Desculpe, mas isso não está relacionado a filmes. Pergunte-me sobre filmes, atores ou diretores!"}
        