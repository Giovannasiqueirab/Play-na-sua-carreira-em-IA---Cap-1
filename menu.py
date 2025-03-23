# menu.py
from cadastro import cadastrar_cultura  # Importa a função para cadastrar uma nova cultura
from plantio import adicionar_dados  # Importa a função para adicionar dados de plantio

# Função para visualizar as culturas cadastradas
def ver_culturas(culturas):
    # Verifica se há culturas cadastradas
    if not culturas:
        print("\nNenhuma cultura cadastrada.")
        return

    # Exibe as culturas cadastradas
    print("\nCulturas Cadastradas:")
    for i, cultura in enumerate(culturas):
        print(f"{i + 1}. Nome: {cultura.nome}")
        print(f"   Base de Plantio: {cultura.base_plantio}")
        print(f"   Espaçamento: {cultura.espacamento}")
        print("-" * 30)  # Linha para separar visualmente as culturas

# Função para excluir uma cultura cadastrada
def excluir_cultura(culturas):
    # Verifica se há culturas cadastradas
    if not culturas:
        print("\nNenhuma cultura cadastrada.")
        return

    # Exibe as culturas cadastradas para que o usuário possa escolher qual excluir
    print("\nCulturas Cadastradas:")
    for i, cultura in enumerate(culturas):
        print(f"{i + 1}. {cultura.nome} ({cultura.base_plantio})")

    # Pede para o usuário escolher qual cultura excluir
    try:
        escolha = int(input("Escolha o número da cultura que deseja excluir: ")) - 1
        if escolha < 0 or escolha >= len(culturas):
            print("Escolha inválida!")
            return

        # Remove a cultura escolhida e exibe uma mensagem de sucesso
        cultura_removida = culturas.pop(escolha)
        print(f"Cultura '{cultura_removida.nome}' removida com sucesso!")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

# Função do menu principal do programa
def menu():
    culturas = []  # Lista para armazenar as culturas cadastradas

    # Loop infinito para exibir o menu até o usuário escolher sair
    while True:
        # Exibe as opções do menu
        print("\n--- Menu Principal ---")
        print("1. Cadastrar cultura")
        print("2. Adicionar dados de plantio")
        print("3. Ver culturas cadastradas")
        print("4. Excluir cultura")
        print("5. Sair")
        
        # Solicita a escolha do usuário
        opcao = input("Escolha uma opção: ").strip()

        # Condições para executar a ação conforme a escolha do usuário
        if opcao == "1":
            cultura = cadastrar_cultura()  # Chama a função de cadastro de cultura
            if cultura:
                culturas.append(cultura)  # Adiciona a cultura na lista
                print(f"Cultura '{cultura.nome}' cadastrada com sucesso!")
        elif opcao == "2":
            adicionar_dados(culturas)  # Chama a função para adicionar dados de plantio
        elif opcao == "3":
            ver_culturas(culturas)  # Exibe as culturas cadastradas
        elif opcao == "4":
            excluir_cultura(culturas)  # Exclui uma cultura
        elif opcao == "5":
            print("Saindo do programa...")  # Sai do programa
            break
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem para opções inválidas
