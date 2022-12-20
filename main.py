def depositar():
    deposito = float(input("Digite o valor que deseja depositar:\n"))
    carteira = 0 + deposito
    print(f'Seu saldo é: {carteira} reais')
def saque():
    print('hi')
    pass
def extrato():
    print('hi')
    pass

def main():
    while True:
        opcao = int(input("Digite a operação desejada de acordo com o numero correspondente:\n[1] Depósito\n[2] Saque\n[3] Extrato\n-> "))
        if opcao == 1:
            depositar()
        elif opcao == 2:
            saque()
        elif opcao == 3:
            extrato()
        else:
            print("Opção inválida, por favor tente novamente")
            continue
main()