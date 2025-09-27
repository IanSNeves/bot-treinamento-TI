import time

TUTORIAL_MAQUINAS_NOVAS = [
    {
        "titulo": "### SESSÃO 1: Preparação e Início da Instalação do Windows ###",
        "passos": [
            "Requisitos: Pendrive bootável com o Windows 11/10 e nenhuma conexão de internet (Wi-Fi desligado e sem cabo Ethernet).",
            "PASSO 1: Insira o pendrive no computador.",
            "PASSO 2: Ligue o computador e acesse o menu de boot (geralmente pressionando F12, F9, ESC ou DEL ao iniciar).",
            "PASSO 3: Selecione o pendrive como dispositivo de boot."
        ]
    },
    {
        "titulo": "### SESSÃO 2: Configuração Inicial do Windows (OOBE) ###",
        "passos": [
            "PASSO 1: Na tela 'Vamos começar com a região', selecione 'Brasil' e clique em 'Sim'.",
            "PASSO 2: Na tela de layout do teclado, selecione 'Português (Brasil ABNT2)' e clique em 'Sim'.",
            "PASSO 3: Na tela 'Quer adicionar um segundo layout de teclado?', clique em 'Pular'.",
            "PASSO 4: IMPORTANTE: Na tela 'Vamos conectar você a uma rede', clique em 'Eu não tenho internet'."
        ]
    }
]


def start():
    """Menu específico para o guia de novas máquinas."""
    while True:
        print("\n--- Guia de Novas Máquinas ---")
        print("1. Conhecer o processo de configuração (Passo a Passo)")
        print("2. Voltar ao menu anterior")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            conhecer_o_processo()
        elif opcao == '2':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida, tente novamente.")

def conhecer_o_processo():
    """Exibe o tutorial passo a passo, aguardando a interação do usuário."""
    print("\n--- Conhecendo o processo de configuração ---")
    print("Pressione 'Enter' para avançar ou digite 'f' e Enter para finalizar a qualquer momento.\n")
    time.sleep(1)

    for sessao in TUTORIAL_MAQUINAS_NOVAS:
        print(f"\n{sessao['titulo']}\n")
        time.sleep(1)
        for passo in sessao['passos']:
            user_input = input(f"- {passo}\n  (Pressione Enter para continuar...) ")
            
            if user_input.strip().lower() == 'f':
                print("\nProcesso finalizado pelo usuário.")
                return
    
    print("\n--- Fim do Tutorial ---")
