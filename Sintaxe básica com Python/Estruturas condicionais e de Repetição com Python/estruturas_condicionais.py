maior_idade = 18
idade_especial = 17


idade = int(input("Informe a sua idade: "))


if idade >= maior_idade:
    print("Maior de idade. Pode tirar a CNH!")

if idade < maior_idade:
    print("Ainda não pode tirar a CNH.")


if idade >= maior_idade:
    print("Maior de idade. Pode tirar a CNH!")

else:
    print("Ainda não pode tirar a CNH.")


if idade >= maior_idade:
    print("Maior de idade. Pode tirar a CNH!")
elif idade == idade_especial:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")


# Estrutura condicional aninhada

conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo+cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque. Saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

else:
    print("Sistema não reconhece a conta bancária. Entre em contato com a gerência.")


# Estrutura condicional ternária

saldo = 200
saque = 500


status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")