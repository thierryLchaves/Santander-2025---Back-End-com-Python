/*
Comment:
Os comandos listados abaixo são para exemplificações de utilização. 
Portanto são comandos simples que foram demonstrados no decorrer da aula 2 modulo 2 vídeo 4 

*/

-- Adicionando a Primary key nas tabelas
ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT, 
ADD PRIMARY KEY (id);


ALTER TABLE destinos
MODIFY COLUMN id INT AUTO_INCREMENT, 
ADD PRIMARY KEY (id);


ALTER TABLE reservas
MODIFY COLUMN id INT AUTO_INCREMENT, 
ADD PRIMARY KEY (id);

-- Adicionando Foreign Key Na tabela de reserva
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id);

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destino
FOREIGN KEY (id_destino) REFERENCES destinos(id);


-- Alterando tabela inserção de opção 
ALTER TABLE reservas
ADD CONSTRAINT fk_usuarios
FOREIGN key (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;


-- dropando uma constraint 

ALTER TABLE reservas DROP CONSTRAINT fk_reservas_usuarios;