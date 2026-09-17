import sqlite3

def cobrar_cuota(dni, id_deporte, mes, anio, monto, medio_pago='EFECTIVO', observacion=''):
    conexion = sqlite3.connect('club.db')
    cursor = conexion.cursor()

    # 1. Buscar al socio por su DNI para obtener su id_socio
    cursor.execute("SELECT id_socio, nombre, apellido FROM socios WHERE dni = ?", (dni,))
    socio = cursor.fetchone()

    if not socio:
        print(f"❌ Error: No existe ningún socio registrado con el DNI {dni}.")
        conexion.close()
        return

    id_socio, nombre, apellido = socio

    # 2. Verificar que el socio esté inscripto en el deporte
    cursor.execute(
        "SELECT 1 FROM socio_deporte WHERE id_socio = ? AND id_deporte = ?",
        (id_socio, id_deporte)
    )
    if not cursor.fetchone():
        print(f"❌ Error: {nombre} {apellido} no está inscripto/a en ese deporte.")
        conexion.close()
        return

    # 3. Verificar si ya pagó este mismo período para no duplicar el cobro
    cursor.execute(
        """
        SELECT id_pago FROM pagos 
        WHERE id_socio = ? AND id_deporte = ? AND mes_periodo = ? AND anio_periodo = ?
        """,
        (id_socio, id_deporte, mes, anio)
    )
    if cursor.fetchone():
        print(f"⚠️ Atención: {nombre} {apellido} ya tiene registrado el pago del período {mes}/{anio} para este deporte.")
        conexion.close()
        return

    # 4. Insertar el pago en la tabla
    cursor.execute(
        """
        INSERT INTO pagos (id_socio, id_deporte, mes_periodo, anio_periodo, monto, medio_pago, observacion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (id_socio, id_deporte, mes, anio, monto, medio_pago, observacion)
    )

    conexion.commit()
    conexion.close()

    print(f"✅ ¡Pago registrado con éxito para {nombre} {apellido}!")
    print(f"   Deporte ID: {id_deporte} | Período: {mes}/{anio} | Monto: ${monto:,.2f} | Medio: {medio_pago}")


# ==========================================
# PRUEBA DE COBRO: Cobrar cuota a María Gómez
# DNI de María: 42987654 | Deporte: Vóley Mayores (ID 1)
# ==========================================
if __name__ == '__main__':
    print("=== SIMULADOR DE COBRO DE CUOTA ===")
    cobrar_cuota(
        dni='42987654',
        id_deporte=1,
        mes=9,
        anio=2026,
        monto=8500.00,
        medio_pago='TRANSFERENCIA',
        observacion='Comprobante enviado por WhatsApp'
    )