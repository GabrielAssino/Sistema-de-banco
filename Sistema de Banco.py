
def mostrar_menu():

    menu = ('\n[1] Depositar\n'
            '[2] Sacar\n'
            '[3] Extrato\n'
            '[4] Sair\n'
            '=======================')
    print(menu)

def sacar(saldo, limite_saque, extrato):
    if (limite_saque > 0):
        valor = int(input('Quando deseja sacar?\n R$ '))
        if (valor <= valor_limite and valor <= saldo):
            saldo -= valor
            limite_saque -= 1
            extrato.append(f'Saque de R${valor}, seu saldo R${saldo}')
            print(f'Saque realizado com sucesso\n Seu saldo atual R${saldo}')
        else:
            print('Ação indisponivel no momento')
    else:
        print('Voce excedeu o limite de saques diarios, volte amanha')

    return saldo, limite_saque, extrato

def depositar(saldo, extrato):
    valor = int(input('Quanto deseja depositar?\n R$ '))
    saldo += valor
    extrato.append(f'Depósito de R${valor}, seu saldo R${saldo}')  # ✅ Corrigido

    return saldo, extrato  # ✅ Retorna os valores corretamente


saldo = 5000
extrato = []
limite_saque = 3
valor_limite = 500


while True:

    mostrar_menu()
    opcao = int(input('Escolha uma opção: '))

    if (opcao == 1):
        saldo, extrato = depositar(saldo, extrato)

    elif (opcao == 2):
        saldo, limite_saque, extrato = sacar(saldo, limite_saque, extrato)

    elif (opcao == 3):
        print("\n=== Extrato ===")
        if extrato:
            for transacao in extrato:
                print(transacao)
        else:
            print('\nExtrato vazio. Nenhuma transação realizada.')
        print("=======================")

    else:
        print('Opção invalida, tente novamente')
