from flask import Flask,render_template, request, Response
import google as genai
from dotenv import load_dotenv
import os
from time import sleep


load_dotenv()

CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
IA_MODELO = 'gemini-2.5-flash'

app = Flask(__name__)


def bot(prompt):
    maximo_tentativas = 2
    contador = 0
    while true:
        try:
            prompt_do_sistema = f"""Sua função é auxiliar no treinamento de novos colaboradores, realizando perguntas sobre os procedimentos padrões da empresa e ensinando de forma didatica, sem adicionar assuntos, fugir da temática ou pesquisar na internet.
            Você não deve responder perguntas que não sejam sobre os procedimentos da empresa."""

            configuracao_modelo = {
                "temperature":0.1,
                "max_output_tokens": 8192,
            }

            llm = genai.GenerativeModel(
                model_name=IA_MODELO,
                system_instruction=prompt_do_sistema,
                generation_config=configuracao_modelo,
            )


            resposta = llm.generate_content(prompt)

        except Exception as erro:
            contador += 1
            if contador >= maximo_tentativas:
                print(f"Ocorreu um erro: {erro}")
                return "Erro no Gemini: %s" % erro
            sleep(50)
    

@app.route('/') #Rotas html principal
def index():
    return render_template('base.html')

#Rotas para os conteudos da pagina (htmx)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get('msg')
    resposta = bot(prompt)
    return render_template('chat.html')

#rota formulário do chat
"""
@app.route('/enviar-mensagem', methods=['POST'])
def enviar_mensagem():
    from flask import request
    user_message = request.form.get('user_message')
    html_user_message = f' <div class="message message--user"><p>{user_message}</p></div> '
    bot_response = "mensagem predefinida"
    html_bot_response = f' <div class="message message--bot"><p>{bot_response}</p></div> '
    return html_user_message + html_bot_response
"""




if __name__ == '__main__':
    app.run(debug=True)

