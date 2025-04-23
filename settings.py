######################## IMPORTACIONES ########################
from dotenv import load_dotenv
import os


##################### CREACIÓN DE TABLAS SCRIPTS #####################
TABLAS = """
CREATE TABLE IF NOT EXISTS usuarios (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre TEXT NOT NULL,
   email TEXT UNIQUE NOT NULL,
   fecha_registro DATE DEFAULT CURRENT_DATE
);
"""



##################### CONFIGURACIONES #####################
# Carga las variables de entorno
load_dotenv()

# Devuelve la ruta donde estará la BD
def obtener_bd(nombre_bd:str) -> str:
    DB_NAME = os.getenv(nombre_bd)
    DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
    return DB_PATH + DB_NAME
