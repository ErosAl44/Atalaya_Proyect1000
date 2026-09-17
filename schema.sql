-- Creación de tablas para SQLite (Actualizado con días y horarios)

CREATE TABLE IF NOT EXISTS socios (
    id_socio INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento TEXT,
    telefono TEXT,
    contacto_emergencia TEXT,
    estado TEXT CHECK(estado IN ('ACTIVO', 'INACTIVO', 'BECADO')) DEFAULT 'ACTIVO',
    fecha_alta TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS deportes (
    id_deporte INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_deporte TEXT NOT NULL,
    categoria TEXT DEFAULT 'General',
    dias_horarios TEXT, -- Ej: 'Lun y Mié 18:00 a 19:30 hs'
    cuota_mensual REAL NOT NULL,
    estado TEXT CHECK(estado IN ('ACTIVO', 'INACTIVO')) DEFAULT 'ACTIVO'
);

CREATE TABLE IF NOT EXISTS socio_deporte (
    id_socio INTEGER NOT NULL,
    id_deporte INTEGER NOT NULL,
    fecha_inscripcion TEXT DEFAULT CURRENT_DATE,
    PRIMARY KEY (id_socio, id_deporte),
    FOREIGN KEY (id_socio) REFERENCES socios(id_socio) ON DELETE CASCADE,
    FOREIGN KEY (id_deporte) REFERENCES deportes(id_deporte) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS pagos (
    id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
    id_socio INTEGER NOT NULL,
    id_deporte INTEGER,
    mes_periodo INTEGER NOT NULL CHECK(mes_periodo BETWEEN 1 AND 12),
    anio_periodo INTEGER NOT NULL,
    monto REAL NOT NULL,
    fecha_pago TEXT DEFAULT CURRENT_TIMESTAMP,
    medio_pago TEXT CHECK(medio_pago IN ('EFECTIVO', 'TRANSFERENCIA', 'MERCADO_PAGO', 'OTRO')) DEFAULT 'EFECTIVO',
    observacion TEXT,
    FOREIGN KEY (id_socio) REFERENCES socios(id_socio) ON DELETE RESTRICT,
    FOREIGN KEY (id_deporte) REFERENCES deportes(id_deporte) ON DELETE SET NULL
);