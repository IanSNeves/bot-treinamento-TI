from guides import guia_novas_maquinas

def menu_inicial():
    print("Bot de treinamento TI - LABO")
    print("selecione uma opção:")
    print("1. Guia de configuração de novas máquinas")
    print("2. sair")
    return input("Sua escolha: ")

def main():
    while True:
        opcao = menu_inicial()
        if opcao == '1':
            guia_novas_maquinas.start()
        elif opcao == '2':
            print("Consulta encerrada. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
