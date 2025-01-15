import re

def apply_guardrails(response: str) -> str:
    """
    Aplica regras de guardrails para verificar a resposta antes de retorná-la.
    """
    if check_offensive_language(response):
        return "Desculpe, não posso fornecer essa informação. Vamos falar sobre filmes?"
    
    if not check_movie_context(response):
        return "Desculpe, mas isso não está relacionado a filmes. Pergunte-me sobre filmes, atores ou diretores!"
    
    if check_for_links(response):
        return "Desculpe, não posso fornecer links externos. Pergunte-me sobre detalhes dos filmes!"
    
    # Se passar por todos os guardrails, retorna a resposta normal.
    return response

def check_offensive_language(response: str) -> bool:
    """
    Verifica se há palavras ou frases ofensivas no texto.
    """
    offensive_keywords = ["violência", "racismo", "discriminação", "assassinato", "ódio", "abuso"]
    return any(keyword in response.lower() for keyword in offensive_keywords)

def check_movie_context(response: str) -> bool:
    """
    Verifica se a resposta está relacionada a filmes, atores, diretores, etc.
    A função agora é mais inteligente, utilizando expressões regulares e verificações de palavras-chave mais flexíveis.
    """
    allowed_keywords = [
        "filme", "ator", "diretor", "elenco", "série", "trailer", "classificação", 
        "episódio", "produção", "história", "sinopse", "avaliação", "recomendação", 
        "personagem", "data de lançamento", "direção", "similar"
    ]
    
    # Verifica se a resposta contém palavras-chave simples relacionadas ao filme
    if any(keyword in response.lower() for keyword in allowed_keywords):
        return True
    
    # Verifica padrões mais complexos com expressões regulares (ex.: perguntas sobre elenco, diretores, etc.)
    movie_patterns = [
        r"(quem|qual).*elenco.*filme",  
        r"(quem|qual).*ator.*filme",    
        r"qual.*sinopse.*filme",        
        r"(quem|qual).*diretor.*filme",  
        r"qual.*trailer.*filme",        
        r"quando.*lançamento.*filme"    
    ]
    
    # Se algum dos padrões de pergunta for encontrado, é um contexto relevante
    if any(re.search(pattern, response.lower()) for pattern in movie_patterns):
        return True
    
    return False

def check_for_links(response: str) -> bool:
    """
    Verifica se a resposta contém links externos.
    """
    return bool(re.search(r'http[s]?://|www\.|ftp://|mailto:', response, re.IGNORECASE))
