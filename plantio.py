import oracledb
from config_db import get_connection

class PlantioManager:
    def __init__(self):
        self.conn = get_connection()
    
    def __del__(self):
        if self.conn:
            self.conn.close()

    def _calcular_custo_total(self, id_insumo, quantidade_total):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT preco_usd FROM insumos WHERE id_insumo = :1", [id_insumo])
                preco = cursor.fetchone()[0]
                return quantidade_total * preco
        except Exception as e:
            print(f"\n Erro ao calcular custo: {e}")
            return 0

    def adicionar_plantio(self):
        try:
            with self.conn.cursor() as cursor:
                # Listar plantações
                cursor.execute("SELECT id_plantacao, nome FROM plantacoes")
                plantios = cursor.fetchall()
                
                print("\n=== PLANTIOS CADASTRADOS ===")
                for id_plant, nome in plantios:
                    print(f"{id_plant} - {nome}")
                
                id_plantacao = int(input("\nID do plantio: "))
                
                # Obter insumos associados
                cursor.execute("""
                    SELECT i.nome, pi.quantidade_ha, pi.quantidade_total, i.unidade 
                    FROM plantio_insumo pi
                    JOIN insumos i ON pi.id_insumo = i.id_insumo
                    WHERE pi.id_plantacao = :1
                """, [id_plantacao])
                
                insumos = cursor.fetchall()
                
                if not insumos:
                    print("\n Nenhum insumo associado a este plantio!")
                    return
                
                # Calcular custos
                total = 0.0
                print("\n=== CUSTOS ESTIMADOS ===")
                for nome, qtd_ha, qtd_total, unidade in insumos:
                    custo = self._calcular_custo_total(id_insumo, qtd_total)
                    total += custo
                    print(f"- {nome}: {qtd_total:.2f} {unidade} → USD {custo:.2f}")
                
                print(f"\n💵 TOTAL: USD {total:.2f}")

        except Exception as e:
            print(f"\n Erro: {e}")