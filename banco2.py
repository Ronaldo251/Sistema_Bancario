
saldo = 0
limite = 500
extrato = []
numero_saque= 0
limite_saque = 3

while True:
    opcao = input("Digite a operação desejada:\n[d] Depósito\n[s] Sacar\n[e] Extrato\n[q] Sair\n -> ")

    if opcao == 'd':
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato.append("+"+str(valor))
        else:
            print("Por favor digite um valor válido.")
    elif opcao == 's':
        if numero_saque < limite_saque:
            valor = float(input("Digite o valor a ser retirado:\n "))
            if valor <= 500:
                saldo -= valor
                extrato.append("-"+str(valor))
                numero_saque += 1
            else:
                print("O saque máximo é de 500 Reais, por favor digite novamente:\n")
                continue
        else:
            print("Você já excedeu o limite de depósitos diários, por favor retorne amanhã ou fale com a gerência.")
            continue
    elif opcao == 'e':
        print(extrato)
    elif opcao == 'q':
        break