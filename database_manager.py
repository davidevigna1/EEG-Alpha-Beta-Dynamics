import mysql.connector
from config import DB_CONFIG

def inserisci_risultati(id_paziente, nome_canale, alpha, beta, ratio):
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql = "INSERT INTO alpha_analysis (id_paziente, nome_canale, potenza_alpha, potenza_beta, ratio_ab) VALUES (%s, %s, %s, %s, %s)"
        valori = (id_paziente, nome_canale, float(alpha), float(beta), float(ratio))

        cursor.execute(sql, valori)
        conn.commit()
        
    except mysql.connector.Error as err:
        print(f"[ERRORE] Database: {err}")
    except Exception as e:
        print(f"[ATTENZIONE] Errore imprevisto nel database: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()