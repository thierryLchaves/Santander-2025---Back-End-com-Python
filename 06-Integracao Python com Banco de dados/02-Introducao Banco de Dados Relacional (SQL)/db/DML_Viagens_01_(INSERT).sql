/*
Comment:
Os comandos abaixos estão listados em ordem de inserção, visto que até o momento da criação  deste arquivo 
não foi realizado a confecção de tabelas, com um integridade referencial entre elas, ou seja as tabelas em
em questão não posuem relacionamentos ou FK/Constraint's informadas. no arquivo de DDL;
*/

INSERT INTO usuarios (id, nome, email, data_nascimento, endereco)VALUES 
(1, 'João da Silva', 'joao@example.com', '1990-05-15','Rua A, 123 Cidade X, Estado Y'), 
(2, 'Maria Santos', 'mria@example.com', '1985-08-22','Rua B, 456 Cidade Y, Estado Z'), 
(3, 'Pedro Souza', 'pedro@example.com', '1998-02-10','Avenida C, 789 Cidade X, Estado Y');

INSERT INTO destinos (id, nome, descricao)
VALUES
(1,'Praia das Tartarugas', 'Uma bela paria com areias brancas e mar cristalino'), 
(2,'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'), 
(3,'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura'),
(1,'Praia do rosa', 'Linda praia');


INSERT INTO reservas (id, id_usuario, id_destino, data, status) VALUES
(1,1,2,'2023-07-10','confirmada'),
(2,2,1,'2023-08-05','pendente'),
(3,3,3,'2023-09-20','cancelada');


INSERT INTO usuarios (nome, email, data_nascimento, rua, numero, cidade, estado) VALUES ('Usuario sem reservas', 'semreservar@teste.com', '1990-10-10', 'Rua','123','cidade','estado');

INSERT INTO viagens.destinos ( nome, descricao) VALUES 
('Destino sem reserva', 'Uma bela praia com areias brancas e mar cristalino');


COMMIT;