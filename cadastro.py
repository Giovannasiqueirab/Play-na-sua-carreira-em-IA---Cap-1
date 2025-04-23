import oracledb
from config_db import get_connection
from cultura import Cultura

# cadastro.py (função associar_insumos_plantio)
def associar_insumos_plantio(id_plantacao):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                
                while True:
                    id_insumo = int(input("\nDigite o ID do insumo (0 para sair): "))
                    if id_insumo == 0:
                        break
                    
                    quantidade_ha = float(input("Quantidade por hectare: "))
                    quantidade_total = quantidade_ha * area_ha  # Mantido
                    
                    cursor.execute("""
                        SELECT quantidade_ha 
                        FROM plantio_insumo 
                        WHERE id_plantio = :plantio_id AND id_insumo = :insumo_id
                    """, {"plantio_id": id_plantacao, "insumo_id": id_insumo})

                    registro_existente = cursor.fetchone()

                    if registro_existente:
                        # Atualiza a quantidade existente
                        nova_quantidade_ha = registro_existente[0] + quantidade_ha
                        nova_quantidade_total = nova_quantidade_ha * area_ha

                        cursor.execute("""
                            UPDATE plantio_insumo 
                            SET 
                                quantidade_ha = :nova_qtd_ha,
                                quantidade_total = :nova_qtd_total
                            WHERE 
                                id_plantio = :plantio_id 
                                AND id_insumo = :insumo_id
                        """, {
                            "nova_qtd_ha": nova_quantidade_ha,
                            "nova_qtd_total": nova_quantidade_total,
                            "plantio_id": id_plantacao,
                            "insumo_id": id_insumo
                        })
                        print(f"✓ Quantidade atualizada: {nova_quantidade_ha} por hectare")

                    else:
                        # Insere novo registro
                        cursor.execute("""
                            INSERT INTO plantio_insumo 
                            (id_plantio, id_insumo, quantidade_ha, quantidade_total)
                            VALUES (:1, :2, :3, :4)
                        """, [id_plantacao, id_insumo, quantidade_ha, quantidade_total])
                        print("✓ Insumo associado pela primeira vez")

                    # =============================================

                conn.commit()
                print("\n✅ Operação concluída com sucesso!")
                
    except Exception as e:
        print(f"\n Erro: {e}")

def cadastrar_plantio():
    try:
        nome = input("\nNome da cultura: ").strip().capitalize()
        
        # Verificar se já existe
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*) FROM plantacoes WHERE UPPER(nome) = UPPER(:nome)", 
                    {'nome': nome}
                )
                if cursor.fetchone()[0] > 0:
                    print(f"\n Erro: Cultura '{nome}' já cadastrada!")
                    return

        # Selecionar região
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_regiao, nome FROM regioes")
                regioes = cursor.fetchall()
                
                if not regioes:
                    print("\n Erro: Nenhuma região cadastrada!")
                    return
                
                print("\n=== REGIÕES DISPONÍVEIS ===")
                for id_regiao, nome_regiao in regioes:
                    print(f"{id_regiao} - {nome_regiao}")
                
                id_regiao = int(input("\nID da região ideal: "))
                
                # Validar região
                cursor.execute("SELECT 1 FROM regioes WHERE id_regiao = :id_regiao", {'id_regiao': id_regiao})
                if not cursor.fetchone():
                    print("\n Região inválida!")
                    return

        # Selecionar base de plantio
        bases = {
            '1': ('quadrado', '2m x 2m'),
            '2': ('retangulo', '80 cm entre linhas'),
            '3': ('triangulo', '50 cm entre plantas'),
            '4': ('hexagono', '1m entre linhas'),
            '5': ('linhas_paralelas', '70 cm entre fileiras')
        }
        
        print("\n=== BASE DE PLANTIO ===")
        for opcao, (base, desc) in bases.items():
            print(f"{opcao}. {base.capitalize()} ({desc})")
        
        opcao = input("\nOpção: ").strip()
        if opcao not in bases:
            print("\n Opção inválida!")
            return
            
        base_plantio, espacamento = bases[opcao]

        # Coletar dimensões
        print("\n=== DIMENSÕES ===")
        if base_plantio == 'quadrado':
            lado = float(input("Lado (metros): "))
            comprimento = largura = lado
        elif base_plantio == 'retangulo':
            comprimento = float(input("Comprimento (metros): "))
            largura = float(input("Largura (metros): "))
        elif base_plantio == 'triangulo':
            base_tri = float(input("Base (metros): "))
            altura = float(input("Altura (metros): "))
            comprimento, largura = base_tri, altura
        elif base_plantio == 'hexagono':
            lado_hex = float(input("Lado do hexágono (metros): "))
            comprimento = largura = lado_hex
        else:  # linhas_paralelas
            comprimento = float(input("Comprimento total (metros): "))
            largura = float(input("Distância entre linhas (metros): "))

        # Calcular área
        cultura = Cultura(nome, base_plantio, espacamento, id_regiao)
        area_m2 = cultura.calcular_area(comprimento, largura)
        area_ha = area_m2 / 10000  # Converter para hectares

        # Coletar época
        epoca = input("\nÉpoca de plantio (ex: Verão, Inverno): ").strip()

        # Inserir no banco
        with get_connection() as conn:
            with conn.cursor() as cursor:
                id_plantacao = cursor.var(oracledb.NUMBER)
                
                cursor.execute("""
                    INSERT INTO plantacoes 
                    (nome, id_regiao_ideal, base_plantio, espacamento, epoca, area_ha, comprimento, largura)
                    VALUES (:nome, :id_regiao, :base_plantio, :espacamento, :epoca, :area_ha, :comprimento, :largura)
                    RETURNING id_plantacao INTO :id_plantacao
                """, {
                    'nome': nome,
                    'id_regiao': id_regiao,
                    'base_plantio': base_plantio,
                    'espacamento': espacamento,
                    'epoca': epoca,
                    'area_ha': area_ha,
                    'comprimento': comprimento,
                    'largura': largura,
                    'id_plantacao': id_plantacao
                })
                
                conn.commit()
                id_plantacao = id_plantacao.getvalue()[0]
                print(f"\n✅ Plantio cadastrado! ID: {id_plantacao} | Área: {area_ha:.2f} ha")

                # Associar insumos
                if input("\nAssociar insumos agora? (S/N): ").upper() == 'S':
                    associar_insumos_plantio(id_plantacao)

    except ValueError:
        print("\n Valor inválido! Use números.")
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"\n Erro Oracle ({error.code}): {error.message}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")