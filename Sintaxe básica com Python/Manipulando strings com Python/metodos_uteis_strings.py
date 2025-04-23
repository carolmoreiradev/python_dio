nome = "cAroL"

# letras maiusculas e minusculas

print(nome.upper())
print(nome.lower())
print(nome.title())


# removendo espaços

texto = "   Olá, mundo "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")


# juncao e centralizacao

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))

print("P-y-t-h-o-n")

for letra in menu:
    print(letra, end = "-")
print()

print("-".join(menu))