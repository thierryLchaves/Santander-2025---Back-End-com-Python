def processar_reservas():
    
    confirmadas = []
    recusadas = []
    
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))


    for solicitado in reservas_solicitadas:
        if solicitado in quartos_disponiveis:
            confirmadas.append(solicitado)
        else:
            recusadas.append(solicitado)

    confirmadas.sort()
    recusadas.sort()
    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()