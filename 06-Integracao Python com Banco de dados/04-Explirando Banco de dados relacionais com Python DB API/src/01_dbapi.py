import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

pasta_raiz = ROOT_PATH.parents[0]

NEW_ROOTH_PATH = pasta_raiz / "database/meu_banco.db"
conn = sqlite3.connect(NEW_ROOTH_PATH)
cur = conn.cursor()
cur.row_factory = sqlite3.Row


def criar_tabela(cursor):
    cur.execute(
        "CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(100), email varchar(150))"
    )
    conn.commit()


def inseir_registro(conxao, cursor, nome, email):
    data = (nome, email)
    cur.execute("INSERT INTO clientes(nome, email) VALUES (?,?)", data)
    conn.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cur.execute("UPDATE clientes SET nome = ?, email=? WHERE ID = ?", data)
    conn.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cur.execute("DELETE FROM clientes WHERE ID = ?", data)
    conn.commit()


def inserir_muitos(conexao, cursor, dados):
    cur.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conn.commit()


dados = [
    ("Larissa", "lalapinksil@gmil.com"),
    ("chappie", "guilherme@gmil.com"),
    ("Melaine", "melaine245@gmil.com"),
]


def recuperar_cliente(conexao, cursor, id):
    cur.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cur.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY NOME;")


clientes = listar_clientes(cursor=cur)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(conexao=conn, cursor=cur, id=3)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])
