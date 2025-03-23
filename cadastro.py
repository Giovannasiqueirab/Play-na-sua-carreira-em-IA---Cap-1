# cadastro.py
# Importa a classe Cultura do módulo cultura
from cultura import Cultura

# Função que vai cadastrar uma nova cultura
def cadastrar_cultura():
    # Solicita ao usuário o nome da cultura e faz algumas formatações para garantir que o nome tenha
    # a primeira letra maiúscula e não tenha espaços no início ou fim.
    nome = input("Digite o nome da cultura: ").strip().capitalize()

    # Exibe as opções de bases de plantio para o usuário escolher
    print("\nEscolha a base de plantio:")
    print("A. Quadrado")
    print("B. Retângulo")
    print("C. Triângulo Equilátero")
    print("D. Hexágono")
    print("E. Linhas Paralelas")

    # O usuário digita a opção correspondente à base de plantio
    escolha_base = input("Digite a letra correspondente à base de plantio: ").strip().lower()

    # Verifica qual base de plantio foi escolhida e define o nome da base e o espaçamento correspondente
    if escolha_base == "a":
        base_plantio = "quadrado"
        espacamento = "2m x 2m"  # Espaçamento comum para o plantio em quadrado
    elif escolha_base == "b":
        base_plantio = "retangulo"
        espacamento = "80 cm entre linhas e 30 cm entre plantas"  # Espaçamento típico para o retângulo
    elif escolha_base == "c":
        base_plantio = "triangulo"
        espacamento = "3 cm entre plantas e 20 cm entre fileiras"  # Espaçamento típico para o triângulo equilátero
    elif escolha_base == "d":
        base_plantio = "hexagono"
        espacamento = "20-30 cm entre plantas"  # Espaçamento recomendado para o hexágono
    elif escolha_base == "e":
        base_plantio = "linhas_paralelas"
        espacamento = "70-80 cm entre fileiras e 20-25 cm entre plantas"  # Espaçamento para as linhas paralelas
    else:
        # Se o usuário digitou uma opção inválida, é mostrado um erro e a função é interrompida
        print("Opção inválida!")
        return None

    # Retorna um objeto da classe Cultura, com o nome da cultura, base de plantio e o espaçamento
    return Cultura(nome, base_plantio, espacamento)
