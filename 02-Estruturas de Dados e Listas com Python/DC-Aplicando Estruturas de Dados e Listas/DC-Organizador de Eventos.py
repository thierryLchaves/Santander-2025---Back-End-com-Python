# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

for _ in range(n):
    entrada = input().strip()
    

    nome, tema = [item.strip() for item in entrada.split(',')]
    
    if tema in eventos:
            eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]


for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")