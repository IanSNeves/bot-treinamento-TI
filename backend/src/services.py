from gerenciar_historico import *
from database import db
from models import BaseDeConhecimento
import google.generativeai as genai
from sqlalchemy import or_
import markdown
from config import llm
from configura_llm import bot

chat_session = llm.start_chat(history=[])

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
        print(f"historico: {history}") 
        
        return texto_contexto
    except Exception as e:
        print(f"Erro na busca: {e}")
        return ""