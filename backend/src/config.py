import google.generativeai as genai
from dotenv import load_dotenv
import os


IA_MODELO = 'gemini-2.5-flash'

PROMPT_DO_SISTEMA = """Você é um assistente interno da empresa Pixeon.
REGRA DE OURO: Você deve responder APENAS com base nas 'INFORMAÇÕES DO SISTEMA' fornecidas.
- Se a resposta não estiver no texto abaixo, diga educadamente: 'Desculpe, não tenho essa informação na minha base de conhecimento interna.'
- NÃO use seu conhecimento externo para inventar tutoriais.
- Caso não haja contexto no banco de dados, diga que não recebeu treinamento, mas alguns problemas podem ser resolvidos com apoio de materiais na internet, se possível analize algumas fontes que possam ajudar na resolução, mas sempre analize antes de responder para manter coerencia..
- Seja direto e use formatação clara (listas, negrito).
- Acesse sempre o histórico de mensagens, e recupere informações ditas anteriormente.
"""

CONFIGURACAO_MODELO = {
    "temperature": 0.5,
    "max_output_tokens": 2000,
    "top_p": 0.9, # Analisa a semelhança das palavras caso haja digitação errada, quanto mais proximo de 1 maior o critério
    "top_k": 64,
}

llm = genai.GenerativeModel(
    model_name=IA_MODELO,
    system_instruction=PROMPT_DO_SISTEMA,
    generation_config=CONFIGURACAO_MODELO,
)