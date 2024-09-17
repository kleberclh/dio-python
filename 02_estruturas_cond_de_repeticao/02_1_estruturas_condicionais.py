# if / if-else / elif

# if aninhado
# if ternario

saldo = 2000
saque = float(input("Informe o valor do saque: "))

# if
if saldo >= saque:
    saldo -= saque  
    print("Realizando saque!")
    print(f"Saldo: {saldo}")
    
if saldo < saque:
    print("Saldo insuficiente!")
    
# if else
if saldo >= saque:
    saldo -= saque  
    print("Realizando saque!")
    print(f"Saldo: {saldo}")
    
else:
    print("Saldo insuficiente!")
    
# if elif else
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quatia para o saque: "))
    # ... continua o codigo do programa

elif opcao == 2:
    print("Exibindo o extrato")
    # ... continua o codigo do programa

else:
    print("Opção inválida!")
                  




