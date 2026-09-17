import sqlite3

conexion = sqlite3.connect('club.db')
cursor = conexion.cursor()

# Leer y ejecutar el archivo seed.sql
with open('seed.sql', 'r', encoding='utf-8') as archivo_sql:
    script_sql = archivo_sql.read()

cursor.executescript(script_sql)

conexion.commit()
conexion.close()

print("¡Datos de prueba cargados con éxito!")