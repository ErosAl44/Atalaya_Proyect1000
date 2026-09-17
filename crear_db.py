import sqlite3

# Crea o abre el archivo de la base de datos
conexion = sqlite3.connect('club.db')
cursor = conexion.cursor()

# Lee tu archivo schema.sql y ejecuta todas las consultas
with open('schema.sql', 'r', encoding='utf-8') as archivo_sql:
    script_sql = archivo_sql.read()

cursor.executescript(script_sql)

conexion.commit()
conexion.close()

print("¡La base de datos club.db se creó correctamente!")