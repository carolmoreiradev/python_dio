class cachorro:
    def __init__(self, nome, cor, acordado = True):         # __init__ sempre éé executado quando uma instância é criada
        print("Inicializando classe...")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def __del__(self):
        print("Removendo a instância da classe...")

    def falar(self):
        print("Au au")

def criar_cachorro():
    c = cachorro("Simba", "branco e preto", False)
    print(c.nome)

c = cachorro("Chappie", "caramelo")
c.falar()

print("Olá, mundo")

del c

print("Olá, mundo")
print("Olá, mundo")

criar_cachorro()