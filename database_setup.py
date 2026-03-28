import mysql.connector
from config import DB_CONFIG

def setup_database():
    config_no_db = DB_CONFIG.copy()
    db_name = config_no_db.pop("database")
    
    try:
        conn = mysql.connector.connect(**config_no_db)
        cursor = conn.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"[OK] Database '{db_name}' verificato/creato.")
        
        cursor.execute(f"USE {db_name}")
        
        cursor.execute("DROP TABLE IF EXISTS alpha_analysis")
        
        query_tabella = """
        CREATE TABLE alpha_analysis (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_paziente INT NOT NULL,
            nome_canale VARCHAR(50),
            potenza_alpha DOUBLE,
            potenza_beta DOUBLE,
            ratio_ab DOUBLE,
            data_analisi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(query_tabella)
        print("[OK] Tabella 'alpha_analysis' resettata e creata correttamente con colonna 'nome_canale'.")
        
        conn.commit()
    except mysql.connector.Error as err:
        print(f"[ERRORE] Durante il setup: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    setup_database()
