import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

pasta_raiz = ROOT_PATH.parents[0]

NEW_ROOTH_PATH = pasta_raiz / "database/meu_banco.db"
conn = sqlite3.connect(NEW_ROOTH_PATH)
cur = conn.cursor()
cur.row_factory = sqlite3.Row


id_cliente = input("Informe o id do cliente: ")
cur.execute(f"SELECT * FROM clientes WHERE ID ={id_cliente} ")
clientes = cur.fetchall()
for cliente in clientes:
    print(dict(cliente))
