menu = """
    ==== MENU ====

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

"""

saldo = 1000
limite_saque = 500
numero_saque = 0
maximo_saque = 3
extrato = ""


while(True):

    print("\nSeja bem-vindo(a) ao DevBank!\n")

    print(menu)

    operacao = input("Digite a operação desejada: ")

    if operacao == "1":
        valor_deposito = float(input("\n\nDigite o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

            print("\nDepósito realizado com sucesso!")
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

        else:
            print("\nValor inválido. Refaça a operação.")


    elif operacao == "2":
        valor_saque = float(input("\nDigite o valor do saque: "))

        if valor_saque > saldo:
            print(f"\nSaldo insuficiente. Refaça a operação")

        elif valor_saque > limite_saque:
            print(f"\nValor máximo para saque excedido. Seu limite é R$ 500,00")

        elif numero_saque >= maximo_saque:
            print(f"\nLimite diário para saque excedido.")

        elif valor_saque <= saldo:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"

            print("\nSaque realizado com sucesso!")

            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

        else:
            print("\nValor inválido. Refaça a operação.")


    elif operacao == "3":
        print("\n\n    ==== EXTRATO ====\n")

        if not extrato:
            print("Não foram realizadas movimentações bancárias.")

        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")

    elif operacao == "0":
        break

    else:
        print("\nOpção inválida. Escolha novamente.")