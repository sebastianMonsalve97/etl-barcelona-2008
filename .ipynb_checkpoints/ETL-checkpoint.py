import sqlite3
import pandas as pd
import logging
import os

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename='logs/proyecto.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------- EXTRACT ----------------
def extract_match_data():
    try:
        conn = sqlite3.connect("database.sqlite")
        logging.info("Conexión establecida con la base de datos.")

        query = """
        SELECT 
            m.match_api_id, 
            m.date, 
            m.home_team_goal, 
            m.away_team_goal,
            th.team_long_name AS home_team_name,
            ta.team_long_name AS away_team_name
        FROM Match m
        LEFT JOIN Team th ON m.home_team_api_id = th.team_api_id
        LEFT JOIN Team ta ON m.away_team_api_id = ta.team_api_id
        """

        df = pd.read_sql_query(query, conn)
        conn.close()
        logging.info(f"Extracción exitosa. Registros obtenidos: {len(df)}")
        return df

    except Exception as e:
        logging.error(f"Error en la extracción de datos: {e}")
        return pd.DataFrame()

# ---------------- TRANSFORM ----------------
def transform_data(df):
    try:
        df['date'] = pd.to_datetime(df['date'])

        df = df[
            (df['home_team_name'].str.contains("Barcelona", na=False)) |
            (df['away_team_name'].str.contains("Barcelona", na=False))
        ]

        df = df[(df['date'] >= '2008-07-01') & (df['date'] <= '2009-06-30')]

        df = df.dropna()

        if df.empty:
            logging.warning("⚠️ El dataframe resultante está vacío luego de la validación.")
        else:
            logging.info(f"✅ Transformación completada. Registros finales: {len(df)}")

        return df

    except Exception as e:
        logging.error(f"❌ Error durante la transformación: {e}")
        return df

# ---------------- LOAD ----------------
def load_data(df, output_path="data/barcelona_2008_2009.csv"):
    try:
        os.makedirs("data", exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info(f"Archivo CSV guardado exitosamente en: {output_path}")
        print(f"✅ Archivo guardado en: {output_path}")

    except Exception as e:
        logging.error(f"Error al guardar archivo CSV: {e}")
        print("❌ Ocurrió un error al guardar el archivo.")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    df_raw = extract_match_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)
