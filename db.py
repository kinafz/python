import psycopg2
from datetime import datetime
from config import db_host, db_port, db_name, db_user, db_password
from logger import logger
import os

conn_params = {
    'host': db_host,
    'port': db_port,
    'database': db_name,
    'user': db_user,
    'password': db_password,
}

conn=None
cursor=None

def updateDb(connection, folder_path="sql"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_dir, folder_path)

    scripts = sorted([
        f for f in os.listdir(folder_path)
        if f.endswith(".sql")
    ])

    with connection.cursor() as cursor:
        for script_file in scripts:
            script_path = os.path.join(folder_path, script_file)
            logger.info(f"\nExécution du script : {script_file}")
            
            with open(script_path, "r", encoding="utf-8") as file:
                sql_commands = file.read()
            try:
                for statement in sql_commands.strip().split(";"):
                    if statement.strip():
                        cursor.execute(statement)
                connection.commit()
                logger.info("Terminé avec succès.")
            except Exception as err:
                logger.error(f"Erreur dans {script_file} : {err}")
                connection.rollback()
                exit(1)

try:
    conn=psycopg2.connect(**conn_params)
    updateDb(conn)
except Exception as e:
    logger.critical(-f"Erreur: {str(e)}")
    exit(1)
    
def insert_data(app_name: str, status: str, response_time: float):
    with conn.cursor() as cursor:
        insert_query = """
            INSERT INTO t_app_status ("date", app_name, status, response_time)
            VALUES (%s, %s, %s, %s)
        """
        data = (datetime.now(), app_name, status, response_time)
        cursor.execute(insert_query, data)
        conn.commit()
        logger.info(f"Insertion réussie pour l'application {app_name}")
