def verfica_urgencia(idade, status):
    
    # CORREÇÃO 1: A idade de prioridade é 60 anos ou mais (>=).
    if idade >= 60 and status.lower() == 'urgente':
        return 1  # Prioridade máxima: Idoso e Urgente
    elif status.lower() == 'urgente':
        return 2  # Prioridade 2: Não-idoso, mas Urgente
    elif idade >= 60:
        return 3  # Prioridade 3: Idoso, sem urgência
    else:
        return 4  # Pr
# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []
lista_prioridade = []

# Loop para entrada de dados
for ordem_chegada in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)

    prioridade = verfica_urgencia(idade,status)

    lista_prioridade.append((prioridade,-idade,ordem_chegada,nome))

lista_prioridade.sort()

nomes_ordenados = [nome for prioridade, neg_idade, ordem, nome in lista_prioridade]

print(f"Ordem de Atendimento: {', '.join(nomes_ordenados)}")
