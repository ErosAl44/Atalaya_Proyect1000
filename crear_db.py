import sqlite3
import os

# Si el archivo de la base de datos ya existe, lo elimina para reconstruirlo desde cero
if os.path.exists('club.db'):
    os.remove('club.db')

conexion = sqlite3.connect('club.db')
cursor = conexion.cursor()

with open('schema.sql', 'r', encoding='utf-8') as archivo_sql:
    script_sql = archivo_sql.read()

cursor.executescript(script_sql)

conexion.commit()
conexion.close()

print("¡La base de datos club.db se creó correctamente con el esquema actualizado!")