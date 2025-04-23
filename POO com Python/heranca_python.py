class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhão(Veiculo):
    # definindo novo construtor
    def __init__(self, cor, placa, numero_rodas, carregado):

        # quando defino um novo construtor, posso sobrescrever os atributos do objeto
        # o método super permite que eu reaproveite os atributos da classe mãe
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim," if self.carregado else "Não"} está carregado")


moto = Motocicleta("preta", "ABC-1234", 2)
# moto.ligar_motor()

carro = Carro("branco", "XDE-0098", 4)
# carro.ligar_motor()

caminhão = Caminhão("roxo", "GFT-8712", 8, True)
# caminhão.ligar_motor()
# caminhão.esta_carregado()

print(moto)
print(carro)
print(caminhão)