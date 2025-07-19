# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",
}

# # Entrada do usuário
usuario = input().strip()
senha = input().strip()


def checar_usuario_senha(usuario, senha):
    resultado = ""
    for check_usuario, check_senha in usuarios.items():
        if check_usuario == usuario:
            if check_senha == senha:
                resultado = "Acesso permitido"
            else:
                resultado = "Usuário ou senha incorretos"

    return resultado


print(checar_usuario_senha(usuario, senha))
