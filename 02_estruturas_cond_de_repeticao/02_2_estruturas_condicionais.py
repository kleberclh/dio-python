conta_normal = True  # Defina como True se a conta for normal
conta_universitaria = False  # Defina como True se a conta for universitária
saldo = 1000  # Saldo atual da conta
cheque_especial = 500  # Limite do cheque especial
saque = 1200  # Valor que deseja sacar

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
