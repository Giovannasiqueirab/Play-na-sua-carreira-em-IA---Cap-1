from config_db import get_connection

class Cultura:
    def __init__(self, nome=None, base_plantio=None, espacamento=None, id_regiao_ideal=None):
        self.id = None
        self.nome = nome
        self.base_plantio = base_plantio
        self.espacamento = espacamento
        self.id_regiao_ideal = id_regiao_ideal

    def calcular_area(self, comprimento, largura):
        calculos = {
            'quadrado': lambda c, l: c * c,
            'retangulo': lambda c, l: c * l,
            'triangulo': lambda c, l: (c * l) / 2,
            'hexagono': lambda c, l: (3 * (c ** 2) * (3 ** 0.5)) / 2,
            'linhas_paralelas': lambda c, l: c * l
        }
        
        if self.base_plantio not in calculos:
            raise ValueError(f"Base de plantio inválida: {self.base_plantio}")
            
        return calculos[self.base_plantio](comprimento, largura)

    def salvar_no_banco(self): 
        pass  