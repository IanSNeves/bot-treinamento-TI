import os 
import google as genai
from dotenv import load_dotenv

load_dotenv()

SYSTEM_INSTRUCTION = """Sua função é auxiliar no treinamento de novos colaboradores, realizando perguntas sobre os procedimentos padrões da empresa e ensinando de forma didatica, sem adicionar assuntos, fugir da temática ou pesquisar na internet.

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
        chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": [SYSTEM_INSTRUCTION]
            },
            {
                "role": "model",
                "parts": ["Entendido. Estou pronto para auxiliar. Como o assunto ainda não foi definido, informarei que estou em manutenção."]
            }
        ])

        while (user_prompt := input("Como posso te ajudar? ")).lower() != 'sair':
            response = chat.send_message(user_prompt, stream=True)
            for chunk in response:
                print(chunk.text, end="")
            print() # Adiciona uma nova linha no final da resposta
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
