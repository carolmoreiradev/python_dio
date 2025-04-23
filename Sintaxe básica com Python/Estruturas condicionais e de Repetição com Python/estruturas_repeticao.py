# Estrutura 'for'

texto = input("Informe um texto: ")
vogais = "AEIOU"

# Exemplo utilizando um iterável (objeto conhecido)

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()     # adiciona quebra de linha


# Exemplo com range

for numero in range(0, 51, 5):
    print(numero, end=" ")

print()


# Estrutura 'while'

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nossos serviços!")


# Estrutura break


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)


for numero in range(100):

    if numero == 10:
        break
    
    print(numero, end = " ")


for numero in range(100):

    if numero % 2 == 0:
        continue
    
    print(numero, end = " ")