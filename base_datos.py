######################## IMPORTACIONES ########################
import sqlite3 as base_datos
import logging
from settings import obtener_bd, TABLAS


# Configuración básica de logging para mostrar mensajes
logging.basicConfig(level=logging.INFO, format="\n%(levelname)s: %(message)s")


######################## CLASE ########################
# Clase que gestiona toda la base de datos
class BaseDatos:

    # CONSTRUCTOR
    def __init__(self, nombre_bd:str, tablas:str):
        """_summary_
        Args:
            nombre_bd (str): Almacena el nombre de la variable de entorno de la BD
            tablas (str): Almacena las tablas que se quieren crear en la BD
        """

        # ATRIBUTOS DE CLASE
        self.DB = nombre_bd

        # Crea las tablas de la BD cuando se instancia
        self.ejecutar(tablas)


    # EJECUTA LAS CONSULTAS
    def ejecutar(self, script:str, parametros="") -> tuple:
        """_summary_
        Args:
            script (str): Almacena el script que será ejecutado
            parametros (str, optional): Si necesita parametros, aqui se almacenan para ser ejecutados

        Returns:
            tuple: Devulve la consulta (si hay), devuelve si se ha podido ejecutar o no
        """

        # Establecer la conexión con la base de datos
        with base_datos.connect(self.DB) as conexion:
            cursor = conexion.cursor()
            consulta = ""

            try:
                # Activa las claves foraneas de la BD
                cursor.execute("PRAGMA foreign_keys = ON;")

                # Si es una tabla ejecuta este cursor
                if "CREATE TABLE" in script[:15]:
                    cursor.executescript(script)

                # Las demas consultas son ejecutadas mediente este cursor
                else:
                    consulta = cursor.execute(script, parametros).fetchall()

                # Guardar los cambios en la base de datos
                conexion.commit()

                # Devuelve si la consulta ha sido exitosa o no
                if cursor.rowcount == 0:
                    return consulta, f"🟥 Sin éxito."
                else:
                    return consulta, f"✅ Éxito."
                
            # Devuelve un error si los hay
            except base_datos.Error as e:
                return [], f"⛔ {e}"

            # Cierra la conexión
            finally:
                cursor.close()


    # INSECCIÓN DE DATOS EN LAS TABLAS
    def insert_into(self, nombre_tabla:str, parametros_nombre:tuple, parametros_valores:tuple):
        """_summary_
        Args:
            nombre_tabla (str): Nombre de la tabla
            parametros_nombre (tuple): Tupla de (str)s con el mismo nombre de las columnas
            parametros_valores (tuple): Tupla de valores a insertar en las columnas
        """

        numero_campos = ("?," * len(parametros_valores)).rstrip(",")
        consulta, mensaje = self.ejecutar(f"INSERT INTO {nombre_tabla} {parametros_nombre} VALUES ({numero_campos})", parametros_valores)

        if "✅" in mensaje:
            logging.info(mensaje)
            return True

        else:
            logging.error(mensaje)
            return False


    # CONSULTA DE DATOS EN LAS TABLAS
    def select(self, nombre_tabla:str, parametros:dict, filtro:str, parametro_filtro:tuple):
        """_summary_
        Args:
            nombre_tabla (str): Nombre de la tabla
            parametros (dict): Diccionario con {nombre_print:numero_columna_bd}
            filtro (str): Nombre de la columna (WHERE) (Si necesitas filtro)
            parametro_filtro (tuple): Tupla con el valor (Si necesitas filtro)
        """

        if filtro: filtro = f"WHERE {filtro}=?"
        consulta, mensaje = self.ejecutar(f"SELECT * FROM {nombre_tabla} {filtro}", parametro_filtro)

        if consulta:
            for i in consulta:
                impresion = ", ".join(f"{clave}: {i[valor]}" for clave, valor in parametros.items())  
                print(f" - {impresion}")

            if "✅" in mensaje: logging.info(mensaje)
            else: logging.error(mensaje)
        
        else: logging.info("ℹ️  No hay resultados.")


    # ACTUALIZACIÓN DE DATOS EN LAS TABLAS
    def update(self, nombre_tabla:str, parametro_update:str, filtro:str, conjuntos_parametros:tuple):
        """_summary_
        Args:
            nombre_tabla (str): Nombre de la tabla
            parametro_update (str): Nombre de la columna a actualizar
            filtro (str): Nombre de la columna para filtrar (WHERE)
            conjuntos_parametros (tuple): Tupla con los valores anteriores (En orden)
        """

        consulta, mensaje = self.ejecutar(f"UPDATE {nombre_tabla} SET {parametro_update} = ? WHERE {filtro} = ?", conjuntos_parametros)

        if "✅" in mensaje: logging.info(mensaje)
        else: logging.error(mensaje)


    # ELIMINACIÓN DE DATOS EN LAS TABLAS
    def delete(self, nombre_tabla:str, filtro:str, parametros_filtro:tuple):
        """_summary_
        Args:
            nombre_tabla (str): Nombre de la tabla
            filtro (str): Nombre de la columna para filtrar (WHERE)
            parametros_filtro (tuple): Tupla con el valor a eliminar
        """

        consulta, mensaje = self.ejecutar(f"DELETE FROM {nombre_tabla} WHERE {filtro} = ?", parametros_filtro)

        if "✅" in mensaje: logging.info(mensaje)   
        else: logging.error(mensaje)

    
    # CONSULTA AVANZADA
    def consulta_avanzada(self, consulta:str, parametros:tuple, salida:dict):
        """_summary_
        Args:
            consulta (str): Consulta completa
            parametros (tuple): Tupla con los valores necesarios para la consulta
            salida (dict): Diccionario con {nombre_print:numero_columna_bd}
        """

        consulta, mensaje = self.ejecutar(consulta, parametros)

        if consulta:
            for i in consulta:
                impresion = ", ".join(f"{clave}: {i[valor]}" for clave, valor in salida.items())  
                print(f" - {impresion}")

            if "✅" in mensaje: logging.info(mensaje)
            else: logging.error(mensaje)
        
        else: logging.info("ℹ️  No hay resultados.")


######################## INSTANCIAS ########################
# Realiza una instancia de BaseDatos
bd = BaseDatos(obtener_bd("DB"), TABLAS)
