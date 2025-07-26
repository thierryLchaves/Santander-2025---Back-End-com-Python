/*
Comment:
Os comandos abaixos estão listados em ordem de inserção, visto que até o momento da criação  deste arquivo 
não foi realizado a confecção de tabelas, com um integridade referencial entre elas, ou seja as tabelas em
em questão não posuem relacionamentos ou FK/Constraint's informadas. no arquivo de DDL;
Assim como a execução do INSERT. 

*/

CREATE TABLE usuarios_nova (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
  endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do Cliente',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
);


INSERT INTO usuarios_nova
SELECT * from usuarios;