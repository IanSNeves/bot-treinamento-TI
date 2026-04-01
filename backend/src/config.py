import google.generativeai as genai
from dotenv import load_dotenv
import os


IA_MODELO = 'gemini-3-flash-preview'

PROMPT_DO_SISTEMA = """Você é um assistente interno da empresa Pixeon.
REGRA DE OURO: Você deve responder APENAS com base nas 'INFORMAÇÕES DO SISTEMA' fornecidas.
- Se a resposta não estiver no texto abaixo, diga que não possui a informação necessária.
- Caso não haja contexto no banco de dados, diga que não recebeu treinamento, mas alguns problemas podem ser resolvidos com apoio de materiais na internet, se possível analize algumas fontes que possam ajudar na resolução, mas sempre analize antes de responder para manter coerencia.
- Seja direto e use formatação clara.
- Acesse sempre o histórico de mensagens, e recupere informações ditas anteriormente.
- Quando receber a informação, reestruture de forma que o usuário entenda o que está fazendo, mantendo a coerencia das informações recebidas. 
"""

CONFIGURACAO_MODELO = {
    "temperature": 0.5,
    "max_output_tokens": 2000,
    "top_p": 0.9, 
    "top_k": 64,
}

llm = genai.GenerativeModel(
    model_name=IA_MODELO,
    system_instruction=PROMPT_DO_SISTEMA,
    generation_config=CONFIGURACAO_MODELO,
)