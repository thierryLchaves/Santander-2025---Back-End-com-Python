use fenda_biqui;

/*O comando insert, diferente do inserOne, tem como caracteristica, que espera uma array de outros documentos*/
db.clients.insert([{"name":"Patrick", "age":38},{"name":"Bob Esponja"}]);

db.clients.find({});


