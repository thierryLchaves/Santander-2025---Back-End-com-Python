-- Traz apenas os usuario com reservas
SELECT * FROM usuarios us
INNER JOIN reservas rs
	ON us.id = rs.id_usuario;

-- Traz todos os usuario e suas reservas se tiver
SELECT * FROM usuarios us
INNER JOIN reservas rs
	ON us.id = rs.id_usuario;


-- Tras todos os destinos e as reservas se tiverem -- 
SELECT * FROM reservas rs
RIGHT JOIN destinos des
	ON des.id = rs.id_destino;

-- Produz o mesmo resultado que a anterior
SELECT * FROM destinos des
LEFT JOIN reservas rs
	ON des.id = rs.id_destino;

-- SUb consultas
-- Usuários que não fizeram nenhuma reserva
SELECT nome
FROM usuarios
WHERE id NOT IN (SELECT id_usuario FROM reservas);

-- Subconsulta para encontrar os destinos menos populares (com menos reservas):
SELECT nome
FROM destinos
WHERE id NOT IN (SELECT id_destino FROM reservas)
ORDER BY id;

-- contagem de reservas por usuario
SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas
FROM usuarios;