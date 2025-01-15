# Sistema de Chatbot de Cinema 🎬🤖
Este é um chatbot que responde perguntas sobre filmes utilizando a API do OpenAI, FastAPI, Langchain e integração com fontes externas de informações sobre filmes.

## Requisitos
Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x (Estou usando o Python 3.10.11)
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

## Executando o Sistema com Docker

Foi feita a inicialização da configuração para executar o projeto rodando Docker

Devido a alguns problemas na minha máquina, para a questão do wsl do Ubuntu, deixo como default a subida do projeto usando os comando citados na sessão (Executando o Sistema)

## Executando os Testes Unitários 🧪

Para garantir que tudo esteja funcionando corretamente, execute os testes automatizados utilizando o pytest:

```bash
python -m pytest
```

Isso executará todos os testes unitários do sistema.

## Seguindo os padrões de projetos

Foi feita a utilização da biblioteca black para formatar o código em Python.

Para rodar o formatador, usar o comando abaixo

```bash
black .
```

## Documentação das APIS (swagger)

É possível utilizar o swagger também para esse projeto, acessando:

http://127.0.0.1:8000/docs

ou também

http://127.0.0.1:8000/redoc

No caso ainda pode ser melhor configurado para aparecer mais rotas

## Testes de API com cURL 🧑‍💻

1. Qual é o elenco do filme Deadpool?

```
curl -X POST http://localhost:8000/chat/ask \
-H "Content-Type: application/json" \
-d '{
    "question": "Qual é o elenco do filme Deadpool?"
}'
```

2. Qual é a sinopse do filme Deadpool?

```
curl -X POST http://localhost:8000/chat/ask \
-H "Content-Type: application/json" \
-d '{
    "question": "Qual é a sinopse do filme Deadpool?"
}'
```

3. Qual é a avaliação do filme Deadpool?

```
curl -X POST http://localhost:8000/chat/ask \
-H "Content-Type: application/json" \
-d '{
    "question": "Qual é a avaliação do filme Deadpool?"
}'
```

4. Quais são os filmes populares no momento?

```
curl -X POST http://localhost:8000/chat/ask \
-H "Content-Type: application/json" \
-d '{
    "question": "Quais são os filmes populares no momento?"
}'
```

5. Dê-me uma recomendação de filme com base no meu gosto por ação.

```
curl -X POST http://localhost:8000/chat/ask \
-H "Content-Type: application/json" \
-d '{
    "question": "Dê-me uma recomendação de filme com base no meu gosto por ação."
}'
```

6. Quero um filme similar ao Deadpool.

```
curl -X POST http://localhost:8000/chat/ask \
-H "Content-Type: application/json" \
-d '{
    "question": "Quero um filme similar ao Deadpool."
}'
```