# cultura.py

# Definindo a classe Cultura, que representará uma cultura agrícola
class Cultura:
    # Método construtor (__init__) que inicializa os dados de uma cultura
    def __init__(self, nome, base_plantio, espacamento):
        self.nome = nome  # Nome da cultura
        self.base_plantio = base_plantio  # Tipo de base de plantio (quadrado, retângulo, etc.)
        self.espacamento = espacamento  # Espaçamento entre as plantas ou linhas

    # Método para calcular a área da cultura dependendo da base de plantio
    def calcular_area(self, comprimento, largura):
        # Verifica qual base de plantio foi escolhida e calcula a área correspondente
        if self.base_plantio == "quadrado":
            return comprimento * comprimento  # Área do quadrado (lado * lado)
        elif self.base_plantio == "retangulo":
            return comprimento * largura  # Área do retângulo (comprimento * largura)
        elif self.base_plantio == "triangulo":
            return (comprimento * largura) / 2  # Área do triângulo (base * altura / 2)
        elif self.base_plantio == "hexagono":
            # Fórmula para calcular a área de um hexágono regular
            return (3 * (comprimento ** 2) * (3 ** 0.5)) / 2
        elif self.base_plantio == "linhas_paralelas":
            return comprimento * largura  # Área para linhas paralelas (como retângulo)
        else:
            # Caso a base de plantio não seja reconhecida, lança um erro
            raise ValueError("Base de plantio não suportada.")

    # Método para calcular os insumos (fertilizantes) necessários com base na área da cultura
    def calcular_insumos(self, area):
        # Verifica a cultura e calcula os insumos necessários para o cultivo
        # Os valores de insumos variam conforme o tipo de cultura
        if self.nome.lower() in ["cenoura"]:
            npk = 0.1 * area  # NPK 4-14-8
            potassio = 0.05 * area  # Potássio
            return {"NPK 4-14-8": npk, "Potássio": potassio}
        elif self.nome.lower() in ["abóbora", "abobora"]:
            npk = 0.1 * area  # NPK 4-14-8
            nitrogenio = 0.07 * area  # Nitrogênio
            return {"NPK 4-14-8": npk, "Nitrogênio": nitrogenio}
        elif self.nome.lower() in ["cana-de-açúcar", "cana-de-acucar", "cana de açúcar", "cana de acucar"]:
            fosforo = (3 * area) / 1000  # Fósforo (P2O5)
            nitrogenio = (8 * area) / 1000  # Nitrogênio (N)
            potassio = (10 * area) / 1000  # Potássio (K2O)
            return {"Fósforo (P2O5)": fosforo, "Nitrogênio (N)": nitrogenio, "Potássio (K2O)": potassio}
        elif self.nome.lower() in ["algodão", "algodao"]:
            fosforo = (4 * area) / 1000  # Fósforo (P2O5)
            nitrogenio = (6 * area) / 1000  # Nitrogênio (N)
            potassio = (8 * area) / 1000  # Potássio (K2O)
            return {"Fósforo (P2O5)": fosforo, "Nitrogênio (N)": nitrogenio, "Potássio (K2O)": potassio}
        else:
            # Caso a cultura não seja reconhecida, retorna um dicionário vazio
            return {}
