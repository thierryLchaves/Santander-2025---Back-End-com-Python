
/*Para criar um novo databse, bata utilizar o comando Use o nome desajado*/
use fenda_biquini

/*Criando uma collection*/
/*Criação de collection explicita, onde é esperado 2 parâmetros sendo eles
1º Sempre será o nome da collection
2º Será algum Json com alguns parâmetros para configuração da collection*/

db.createCollection("teste", { capped: true, max: 2, size: 2 });

/*Demonstrando a collection*/
show collections;

/*Inserindo dados na collection*/
db.teste.insertOne({ "name": "Teste1" });

/*Listando todos documentos*/
db.teste.find({})

/*Inserindo o 2º registro*/
db.teste.insertOne({ "name": "Teste2" });

/*Inserindo o 3º registro para validar se o parâmetro está sendo aplicado*/
db.teste.insertOne({ "name": "Teste3" });

/*Criando a collection implicitamente*/
db.teste2.insertOne({ "age": 10 });

db.teste2.find({});