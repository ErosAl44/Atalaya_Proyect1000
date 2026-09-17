import sqlite3

# Definimos el mes y año a consultar (ej: Septiembre 2026)
MES = 9
ANIO = 2026

conexion = sqlite3.connect('club.db')
cursor = conexion.cursor()

# Consulta con LEFT JOIN: busca todos los socios inscriptos a un deporte
# y une los pagos. Si p.id_pago es NULL, significa que no registró pago.
query_deudores = """
SELECT 
    s.dni,
    s.nombre || ' ' || s.apellido AS socio,
    s.telefono,
    d.nombre_deporte,
    d.categoria,
    d.cuota_mensual
FROM socio_deporte sd
JOIN socios s ON sd.id_socio = s.id_socio
JOIN deportes d ON sd.id_deporte = d.id_deporte
LEFT JOIN pagos p ON sd.id_socio = p.id_socio 
                 AND sd.id_deporte = p.id_deporte 
                 AND p.mes_periodo = ? 
                 AND p.anio_periodo = ?
WHERE p.id_pago IS NULL 
  AND s.estado = 'ACTIVO';
"""

cursor.execute(query_deudores, (MES, ANIO))
deudores = cursor.fetchall()

print(f"=== LISTADO DE DEUDORES ({MES}/{ANIO}) ===")
if deudores:
    for d in deudores:
        print(f"DNI: {d[0]} | Socio: {d[1]} | Tel: {d[2]} | Deporte: {d[3]} ({d[4]}) | Debe: ${d[5]:,.2f}")
else:
    print("¡Excelente! Todos los socios inscriptos están al día.")

conexion.close()