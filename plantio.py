# plantio.py
# Função para adicionar dados de plantio para uma cultura
def adicionar_dados(culturas):
    # Verifica se há culturas cadastradas
    if not culturas:
        print("\nNenhuma cultura cadastrada. Cadastre uma cultura primeiro.")
        return  # Sai da função caso não haja culturas

    # Exibe as culturas cadastradas para que o usuário possa escolher uma
    print("\nCulturas cadastradas:")
    for i, cultura in enumerate(culturas):
        print(f"{i + 1}. {cultura.nome} ({cultura.base_plantio})")

    # Solicita ao usuário escolher a cultura
    try:
        escolha = int(input("Escolha o número da cultura: ")) - 1
        if escolha < 0 or escolha >= len(culturas):
            print("Escolha inválida!")  # Informa erro caso a escolha seja inválida
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    # Obtém a cultura escolhida
    cultura = culturas[escolha]
    
    # Solicita as dimensões da área de plantio (comprimento e largura)
    try:
        comprimento = float(input("Digite o comprimento da área de plantio (em metros): "))
        largura = float(input("Digite a largura da área de plantio (em metros): "))
    except ValueError:
        print("Por favor, insira valores válidos para comprimento e largura.")
        return

    # Calcula a área da plantação com base na cultura e dimensões fornecidas
    area = cultura.calcular_area(comprimento, largura)
    print(f"\nÁrea de plantio: {area:.2f} m²")  # Exibe a área com 2 casas decimais

    # Calcula os insumos necessários para a cultura na área especificada
    insumos = cultura.calcular_insumos(area)
    
    # Exibe os insumos necessários, se houver
    if insumos:
        print("\nInsumos necessários:")
        for insumo, quantidade in insumos.items():
            print(f"- {quantidade:.2f} kg de {insumo}")  # Exibe a quantidade de cada insumo
    else:
        print("Nenhum insumo necessário para esta cultura.")  # Caso não haja insumos para a cultura
