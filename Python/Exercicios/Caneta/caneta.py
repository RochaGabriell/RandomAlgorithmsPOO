class Caneta:
    def __init__(self, modelo, cor, tampada):
        self.modelo = modelo
        self.cor = cor
        self.tampada = tampada

    def rabiscar(self):
        if self.tampada is True:
            print("A caneta está tampada.")
        else:
            print("Estou escrevendo")

    def tampar(self):
        self.tampada = True

    def destanpar(self):
        self.tampada = False

    def __str__(self):
        return f"Modelo: {self.modelo} - Cor: {self.cor} - Tampada: {self.tampada}."