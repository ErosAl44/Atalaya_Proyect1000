-- Insertar deportes iniciales del club
INSERT INTO deportes (nombre_deporte, categoria, cuota_mensual) VALUES
('Vóley', 'Mayores', 8500.00),
('Vóley', 'Juveniles', 7000.00),
('Fútbol', 'Infantil', 6500.00),
('Básquet', 'General', 7500.00);

-- Insertar socios de prueba
INSERT INTO socios (dni, nombre, apellido, fecha_nacimiento, telefono) VALUES
('40123456', 'Juan', 'Pérez', '1998-05-12', '1122334455'),
('42987654', 'María', 'Gómez', '2001-09-20', '1166778899'),
('45111222', 'Lucas', 'Rodríguez', '2004-03-15', '1133445566');

-- Inscribir socios a deportes
-- Juan a Vóley Mayores (id_socio 1, id_deporte 1)
INSERT INTO socio_deporte (id_socio, id_deporte) VALUES (1, 1);

-- María a Vóley Mayores (id_socio 2, id_deporte 1) y Básquet (id_socio 2, id_deporte 4)
INSERT INTO socio_deporte (id_socio, id_deporte) VALUES (2, 1);
INSERT INTO socio_deporte (id_socio, id_deporte) VALUES (2, 4);

-- Registrar un pago de prueba
-- Juan pagó Vóley de Septiembre 2026
INSERT INTO pagos (id_socio, id_deporte, mes_periodo, anio_periodo, monto, medio_pago, observacion) 
VALUES (1, 1, 9, 2026, 8500.00, 'EFECTIVO', 'Pago registrado en recepción');