
EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";

EXPLAIN SELECT * FROM usuarios us
INNER JOIN reservas rs
ON us.id = rs.id_usuario
WHERE nome = "Maria";


CREATE INDEX idx_nome ON usuarios (nome);

EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";