from cadastro import cadastrar_plantio 
from plantio import PlantioManager
from config_db import get_connection

def ver_plantios():  
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        p.id_plantacao,
                        p.nome AS cultura,
                        r.nome AS regiao_ideal,
                        NVL(p.epoca, 'Não informada') AS epoca,
                        NVL(p.base_plantio, 'Não especificada') AS base_plantio,
                        p.area_ha
                    FROM plantacoes p
                    LEFT JOIN regioes r ON p.id_regiao_ideal = r.id_regiao
                """)
                
                print("\n{:<5} {:<20} {:<15} {:<15} {:<20} {:<10}".format(
                    "ID", "Cultura", "Região Ideal", "Época", "Base de Plantio", "Área (ha)"))
                print("-"*90)
                
                for row in cursor:
                    id_plant, cultura, regiao, epoca, base, area = row
                    regiao = regiao or "N/A"
                    epoca = epoca or "N/A"
                    base = base or "N/A"
                    area = f"{area:.2f}" if area else "N/A"
                    
                    print("{:<5} {:<20} {:<15} {:<15} {:<20} {:<10}".format(
                        id_plant,
                        cultura,
                        regiao[:15],
                        epoca[:15],
                        base[:20],
                        area
                    ))
                    
    except Exception as e:
        print(f"\n Erro ao carregar plantios: {e}")

def menu():
    plantio_manager = PlantioManager()
    
    while True:
        print("\n=== SISTEMA DE GESTÃO AGRÍCOLA ===")
        print("1. Cadastrar novo plantio")
        print("2. Registrar custos de plantio")
        print("3. Ver plantios cadastrados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_plantio()  
        elif opcao == "2":
            plantio_manager.adicionar_plantio()
        elif opcao == "3":
            ver_plantios()  
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()