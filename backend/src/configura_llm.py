from gerenciar_historico import *
from database import db
from models import BaseDeConhecimento
import google.generativeai as genai
from sqlalchemy import or_
import markdown
from config import *

llm = genai.GenerativeModel(
    model_name=IA_MODELO,
    system_instruction=PROMPT_DO_SISTEMA,
    generation_config=CONFIGURACAO_MODELO,
)

chat = llm.start_chat(history=[])

def buscar_contexto(prompt):
    palavras = prompt.split()
    filtros = []
    
    for palavra in palavras:
        if len(palavra) > 3: 
            filtros.append(BaseDeConhecimento.titulo.like(f'%{palavra}%'))
            filtros.append(BaseDeConhecimento.conteudo.like(f'%{palavra}%'))
    
    if not filtros:
        return ""

    try:
        resultados = BaseDeConhecimento.query.filter(or_(*filtros)).limit(3).all()

        texto_contexto = ""
        for item in resultados:
            texto_contexto += f"\n---\nAssunto: {item.titulo}\nConteúdo: {item.conteudo}\n"
        
        print(f"DEBUG - Contexto encontrado: {texto_contexto}") 
        
        return texto_contexto
    except Exception as e:
        print(f"Erro na busca: {e}")
        return ""



def bot(prompt):
    contexto = buscar_contexto(prompt)

    if contexto:
        prompt_final = f"""Use as informações abaixo para responder as perguntas do usuário.
        
        INFORMAÇÕES DO SISTEMA:
        {contexto}
        
        PERGUNTA DO USUÁRIO:
        {prompt}"""
    else:
        prompt_final = PROMPT_DO_SISTEMA + prompt

    if len(chat.history) > 8:
        chat.history = remover_mensagens_antigas(chat.history)

    try:
        resposta = chat.send_message(prompt_final)
        resposta_html = markdown.markdown(resposta.text)
        return resposta_html
    
    
    except Exception as e:
        print(f"Erro: {e}")
        return "Sistema indisponível."