from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH/'NOVO-DIRETORIO'/"novo.txt",'r')
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
except IsADirectoryError as ex:
    print(f'Não foi possível abrir o arquivo: {ex}')
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')
except Exception as exc:
    print(f"ALgum problema ocorreu ao tentar abrir o arquivo: {exc}")

