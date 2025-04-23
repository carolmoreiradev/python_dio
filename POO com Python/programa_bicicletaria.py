class bicicleta:
    def __init__(self,cor,modelo, ano, valor, aro = 18):        # método construtor
        self.cor = cor                                          # atributos
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta")
        print("Bicileta parada!")

    def correr(self):
        print("Vruuuummm...")

    def trocar_marcha(self, nro_marcha):
        print("Trocando a marcha")

        def _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                print("Marcha trocada")

            else:
                print("Não foi possível trocar de marcha")

    def get_cor(self):
        return self.cor


    # Cria uma string para exibir os atributos

    # def __str__(self):
    #     return f"Bicileta: {self.cor}, {self.modelo}, {self.ano},{self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


# Instanciando

b1 = bicicleta("vermelha", "caloi", 2022, 600)
b1.correr()
b1.buzinar()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta("verde", "monark", 200, 189)
print(b2)
bicicleta.buzinar(b2)       # equivalente a b2.buzinar()
print(b2.get_cor())