/*
Comment:
Os comandos listados abaixo são para exemplificações de utilização. 
Portanto são comandos simples que foram demonstrados no decorrer da aula 2 modulo 2 vídeo 3 
*/

UPDATE usuarios
SET
    id = 4
WHERE email = 'teste@teste.com';
COMMIT;


DELETE FROM destinos
where nome = 'Praia do rosa';