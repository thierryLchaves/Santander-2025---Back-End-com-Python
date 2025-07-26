CREATE TABLE viagens.usuarios (
    id INT, 
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário', 
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário', 
    endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do usuário', 
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
); 

CREATE TABle viagens.destinos(
    id INT, 
    nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino', 
    descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE viagens.reservas(
    id INT COMMENT 'Identificado único da reserva', 
    id_usuario INT COMMENT 'Referência ao  ID do usuário que fez a reserva', 
    id_destino INT COMMENT 'Referência ao ID  do usuário que fez a reserva', 
    data DATE COMMENT 'Data da reserva', 
    status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc. )'
);