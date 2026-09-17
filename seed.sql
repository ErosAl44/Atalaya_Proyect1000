-- Insertar deportes iniciales del club con sus horarios
INSERT INTO deportes (nombre_deporte, categoria, dias_horarios, cuota_mensual) VALUES
('Vóley', 'Mayores', 'Mar y Jue 20:00 a 22:00 hs', 8500.00),
('Vóley', 'Juveniles', 'Lun, Mié y Vie 18:00 a 19:30 hs', 7000.00),
('Fútbol', 'Infantil', 'Sáb 10:00 a 12:00 hs', 6500.00),
('Básquet', 'General', 'Mar y Jue 18:30 a 20:00 hs', 7500.00);

-- Insertar socios de prueba
INSERT INTO socios (dni, nombre, apellido, fecha_nacimiento, telefono) VALUES
('40123456', 'Juan', 'Pérez', '1998-05-12', '1122334455'),
('42987654', 'María', 'Gómez', '2001-09-20', '1166778899'),
('45111222', 'Lucas', 'Rodríguez', '2004-03-15', '1133445566');

-- Inscribir socios a deportes
INSERT INTO socio_deporte (id_socio, id_deporte) VALUES (1, 1);
INSERT INTO socio_deporte (id_socio, id_deporte) VALUES (2, 1);
INSERT INTO socio_deporte (id_socio, id_deporte) VALUES (2, 4);

-- Registrar un pago de prueba
INSERT INTO pagos (id_socio, id_deporte, mes_periodo, anio_periodo, monto, medio_pago, observacion) 
VALUES (1, 1, 9, 2026, 8500.00, 'EFECTIVO', 'Pago registrado en recepción');