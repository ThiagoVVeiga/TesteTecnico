# Sistema de Chatbot de Cinema 🎬🤖
Este é um chatbot que responde perguntas sobre filmes utilizando a API do OpenAI, FastAPI, Langchain e integração com fontes externas de informações sobre filmes.

## Requisitos
Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas necessárias:
  - fastapi
  - uvicorn
  - requests
  - openai
  - pytest
  - httpx
  - langchain-openai
  - langchain_community
  - langchain
  - asyncio

## Instalação 🚀
Clone este repositório para o seu ambiente local:

```bash
git clone <url-do-repositorio>
```

Instale as dependências necessárias com o comando abaixo:

```bash
pip install -r requirements.txt
```

## Executando o Sistema 🏃‍♂️💻

Para rodar a aplicação FastAPI, use o seguinte comando:

```bash
$env:OPENAI_API_KEY="SUA_CHAVE_AQUI"
python -m uvicorn app.main:app --reload
```

O servidor estará disponível em http://localhost:8000.

## Executando os Testes Unitários 🧪

Para garantir que tudo esteja funcionando corretamente, execute os testes automatizados utilizando o pytest:

```bash
python -m pytest
```

Isso executará todos os testes unitários do sistema.

## Testes de API com cURL 🧑‍💻

1. Qual é o elenco do filme Deadpool?

```
curl -X 'GET' \
  'http://localhost:8000/perguntar?questao=Qual%20%C3%A9%20o%20elenco%20do%20filme%20Deadpool%20%3F' \
  -H 'accept: application/json'
```

2. Qual é a sinopse do filme Deadpool?

```
curl -X 'GET' \
  'http://localhost:8000/perguntar?questao=Qual%20%C3%A9%20a%20sinopse%20do%20filme%20Deadpool%20%3F' \
  -H 'accept: application/json'
```

3. Qual é a avaliação do filme Deadpool?

```
curl -X 'GET' \
  'http://localhost:8000/perguntar?questao=Qual%20%C3%A9%20a%20avalia%C3%A7%C3%A3o%20do%20filme%20Deadpool%20%3F' \
  -H 'accept: application/json'
```

4. Quais são os filmes populares no momento?

```
curl -X 'GET' \
  'http://localhost:8000/perguntar?questao=Quais%20s%C3%A3o%20os%20filmes%20populares%20no%20momento%20%3F' \
  -H 'accept: application/json'
```

5. Dê-me uma recomendação de filme com base no meu gosto por ação.

```
curl -X 'GET' \
  'http://localhost:8000/perguntar?questao=D%C3%AA-me%20uma%20recomenda%C3%A7%C3%A3o%20de%20filme%20com%20base%20no%20meu%20gosto%20por%20a%C3%A7%C3%A3o.%20' \
  -H 'accept: application/json'
```

6. Quero um filme similar ao Deadpool.

```
curl -X 'GET' \
  'http://localhost:8000/perguntar?questao=Quero%20um%20filme%20similar%20ao%20Deadpool' \
  -H 'accept: application/json'
```