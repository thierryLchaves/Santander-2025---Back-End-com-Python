/*
Comment:
Os comandos listados abaixo são para exemplificações de utilização. 
Portanto são comandos simples que foram demonstrados no decorrer da aula 2 modulo 2 vídeo 4 

*/
-- Excluindo tabela anterior --
DROP table usuarios;

-- Renomeando nova tabela --
ALTER TABLE usuarios_nova RENAME usuarios;

-- Ou opção 2 : Alterar tamanho da coluna endereço -- 
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);




