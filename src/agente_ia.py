import os 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

SYSTEM_INSTRUCTIOM = """Sua função é auxiliar no treinamento de novos colaboradores, realizando perguntas sobre os procedimentos padrões da empresa e ensinando de forma didatica, sem adicionar assuntos, fugir da temática ou pesquisar na internet.

por enquanto não há assunto definido, então apenas diga que está em manutenção."""

def iniciar_chat():
    print("Chat iniciado! \nVocê pode sair desse chat a qualquer momento digitando 'sair'.")

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("\nAPI não encontrada.")
            return

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(model_name='gemini-2.5-flash')
        chat = model.start_chat(history=[])

        user_prompt = input("Como posso te ajudar?")

        while user_prompt.lower() != 'sair':
            response = chat.send_message(user_prompt)
            print(response.text)
            user_prompt = input()
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


