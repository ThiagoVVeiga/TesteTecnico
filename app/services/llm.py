import httpx
from typing import List
from fastapi import APIRouter
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool

# TODO: Implementação aqui da escolha de outros modelos

MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie"
API_KEY = "818306944e112ccf75d496086ac6c42e"

router = APIRouter()


def fetch_movie_id_by_name(movie_name: str) -> str:
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}&language=pt-BR"
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
            data = response.json()
            if data["results"]:
                return data["results"][0]["id"]
            return None
    except httpx.RequestError as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None


def fetch_cast(movie_name: str) -> List:
    movie_id = fetch_movie_id_by_name(movie_name)
    if movie_id:
        try:
            url = f"{MOVIE_API_BASE_URL}/{movie_id}/credits?api_key={API_KEY}&language=pt-BR"
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                return [
                    {"name": member["name"], "character": member["character"]}
                    for member in data["cast"]
                ]
        except httpx.RequestError as e:
            print(f"Erro ao buscar elenco: {e}")
            return []
    return []


def fetch_synopsis(movie_name: str) -> str:
    movie_id = fetch_movie_id_by_name(movie_name)
    if movie_id:
        try:
            url = f"{MOVIE_API_BASE_URL}/{movie_id}?api_key={API_KEY}&language=pt-BR"
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                return data.get("overview", "Sinopse não disponível")
        except httpx.RequestError as e:
            print(f"Erro ao buscar sinopse: {e}")
            return "Sinopse não encontrada"
    return "Sinopse não encontrada"


def fetch_rating(movie_name: str) -> str:
    movie_id = fetch_movie_id_by_name(movie_name)
    if movie_id:
        try:
            url = f"{MOVIE_API_BASE_URL}/{movie_id}?api_key={API_KEY}&language=pt-BR"
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                return f"Avaliação: {data.get('vote_average', 'N/A')} (Baseada em {data.get('vote_count', 0)} votos)"
        except httpx.RequestError as e:
            print(f"Erro ao buscar avaliação: {e}")
    return "Avaliação não encontrada"


def fetch_popular_movies(movie_name: str) -> List:
    try:
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=pt-BR&page=1"
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
            data = response.json()
            return [
                {"name": movie["title"], "id": movie["id"]} for movie in data["results"]
            ]
    except httpx.RequestError as e:
        print(f"Erro ao buscar filmes populares: {e}")
        return []


def fetch_similar_movies(movie_name: str) -> List:
    movie_id = fetch_movie_id_by_name(movie_name)
    if movie_id:
        try:
            url = f"{MOVIE_API_BASE_URL}/{movie_id}/similar?api_key={API_KEY}&language=pt-BR&page=1"
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                return [
                    {"name": movie["title"], "id": movie["id"]}
                    for movie in data["results"]
                ]
        except httpx.RequestError as e:
            print(f"Erro ao buscar filmes semelhantes: {e}")
            return []
    return []


tools = [
    Tool(
        name="Fetch Popular Movies",
        func=fetch_popular_movies,
        description="Busca filmes populares (responda em português, detalhe um pouco mais sobre sua resposta e me mostre uma lista de nomes de filmes populares)",
    ),
    Tool(
        name="Fetch Cast",
        func=fetch_cast,
        description="Busca o elenco de um filme  (responda em português, detalhe um pouco mais sobre sua resposta)",
    ),
    Tool(
        name="Fetch Similar Movies",
        func=fetch_similar_movies,
        description="Busca filmes semelhantes e serve para dar recomendações de filmes por gênero também ou por nome (responda em português, detalhe um pouco mais sobre sua resposta e me mostre uma lista de nomes de filmes similares)",
    ),
    Tool(
        name="Fetch Synopsis",
        func=fetch_synopsis,
        description="Busca a sinopse de um filme (responda em português, detalhe um pouco mais sobre sua resposta)",
    ),
    Tool(
        name="Fetch Rating",
        func=fetch_rating,
        description="Busca a avaliação de um filme (responda em português, detalhe um pouco mais sobre sua resposta)",
    ),
]

llm = ChatOpenAI(temperature=0.7)


def generate_response(question: str) -> str:
    agent = initialize_agent(
        tools,
        llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    response = agent.invoke([question])
    return response["output"]


@router.get("/populares")
def get_popular_movies_route(movie_name: str):
    popular_movies = fetch_popular_movies(movie_name)
    return {"popular_movies": popular_movies}


@router.get("/elenco")
def get_cast_route(movie_name: str):
    cast = fetch_cast(movie_name)
    return {"cast": cast}


@router.get("/sinopse")
def get_synopsis_route(movie_name: str):
    synopsis = fetch_synopsis(movie_name)
    return {"synopsis": synopsis}


@router.get("/avaliacao")
def get_rating_route(movie_name: str):
    rating = fetch_rating(movie_name)
    return {"rating": rating}


@router.get("/semelhantes")
def get_similar_movies_route(movie_name: str):
    similar_movies = fetch_similar_movies(movie_name)
    return {"similar_movies": similar_movies}
