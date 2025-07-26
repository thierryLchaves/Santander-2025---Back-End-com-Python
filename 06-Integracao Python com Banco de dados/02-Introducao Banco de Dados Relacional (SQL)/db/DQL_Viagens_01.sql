/*
Comment:
Os comandos listados abaixo são para exemplificações de utilização. 
Portanto são comandos simples que foram demonstrados no decorrer da aula 2 modulo 2 vídeo 2 
*/

--Select default ou select simples;
SELECT *
FROM usuarios; -- Poderia ser qualquer uma das 3(três) tabelas existentes destinos, viagens ou usuurios

-- Select com condição ou select where
SELECT *
FROM usuarios
where id = 1;

-- SELECT com where, porém com operadores;
SELECT *
FROM usuarios
WHERE id = 1
AND nome LIKE '%João'

SELECT *
FROM usuarios
where id = 1
or nome like "%Maria%"




