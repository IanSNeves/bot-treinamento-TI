from flask import Flask,render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
from time import sleep


load_dotenv()

CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GEMINI)
IA_MODELO = 'gemini-2.5-flash'

app = Flask(__name__)


def bot(prompt):
    maximo_tentativas = 2
    contador = 0

    prompt_do_sistema = f"""Sua função é auxiliar no treinamento de novos colaboradores, realizando perguntas sobre os procedimentos padrões da empresa e ensinando de forma didatica, sem adicionar assuntos, fugir da temática ou pesquisar na internet. Você não deve responder perguntas que não sejam sobre os procedimentos da empresa.
    Por enquanto não há assunto definido, não invente nenhum prossedimento nem padrão para a empresa, informe isso ao usuario e matenha um fluxo simples de conversa, estando proibido de ensinar qualquer assunto."""
    configuracao_modelo = {
        "temperature":0.1,
        "max_output_tokens": 8192,
    }

    llm = genai.GenerativeModel(
        model_name=IA_MODELO,
        system_instruction=prompt_do_sistema,
        generation_config=configuracao_modelo,
    )

    while True:
        try:
            resposta = llm.generate_content(prompt)
            return resposta.text
        except Exception as erro:
            contador += 1
            if contador >= maximo_tentativas:
                print(f"Ocorreu um erro: {erro}")
                return "Erro no Gemini: %s" % erro
            sleep(2)
    

@app.route('/') #Rotas html principal
def index():
    return render_template('base.html')

#Rotas para os conteudos da pagina (htmx)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/chat', methods=['GET'])
def chat():
    prompt = request.form.get('msg')
    resposta = bot(prompt)
    return render_template('chat.html')

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    user_message = request.form.get('user_message')
    bot_response = bot(user_message)
    html_user = f'<div class="message message--user"><p>{user_message}</p></div>'
    html_bot = f'<div class="message message--bot"><p>{bot_response}</p></div>'
    
    return html_user + html_bot    


if __name__ == '__main__':
    app.run(debug=True)

