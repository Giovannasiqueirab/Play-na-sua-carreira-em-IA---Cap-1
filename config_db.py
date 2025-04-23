# config_db.py
import oracledb

# Configurações de conexão
DB_USER = "" 
DB_PASSWORD = ""  
DB_HOST = ""
DB_PORT = 1521
DB_SERVICE = ""

try:
    oracledb.init_oracle_client()
except Exception as e:
    print(f"Aviso: {e}")

def get_connection():
    """Retorna uma conexão com o banco de dados"""
    try:
        dsn = oracledb.makedsn(DB_HOST, DB_PORT, service_name=DB_SERVICE)
        return oracledb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=dsn
        )
    except Exception as e:
        print(f"Erro de conexão: {e}")
        raise