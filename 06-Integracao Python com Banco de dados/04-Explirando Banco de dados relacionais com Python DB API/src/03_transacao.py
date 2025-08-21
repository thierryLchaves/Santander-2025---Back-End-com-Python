import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

pasta_raiz = ROOT_PATH.parents[0]

NEW_ROOTH_PATH = pasta_raiz / "database/meu_banco.db"
conn = sqlite3.connect(NEW_ROOTH_PATH)
cur = conn.cursor()
cur.row_factory = sqlite3.Row

try:
    cur.execute(
        "INSERT INTO clientes (nome,email) values(?,?)", ("Teste 3", "teste3@gmail.com")
    )
    cur.execute(
        "INSERT INTO clientes (id,nome,email) values(?,?,?)",
        (3, "Teste 4", "teste4@gmail.com"),
    )
    conn.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu! {exc}")
    conn.rollback()
