import sqlite3

conexion = sqlite3.connect('club.db')
cursor = conexion.cursor()

# Consultar socios y sus deportes
query = """
SELECT s.nombre, s.apellido, d.nombre_deporte, d.categoria 
FROM socios s
JOIN socio_deporte sd ON s.id_socio = sd.id_socio
JOIN deportes d ON sd.id_deporte = d.id_deporte
"""

cursor.execute(query)
resultados = cursor.fetchall()

print("--- SOCIOS E INSCRIPCIONES ---")
for fila in resultados:
    print(f"Socio: {fila[0]} {fila[1]} | Deporte: {fila[2]} ({fila[3]})")

conexion.close()