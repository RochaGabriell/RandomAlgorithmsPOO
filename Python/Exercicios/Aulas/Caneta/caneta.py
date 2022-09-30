class Caneta:
    def __init__(self, modelo, cor, tampada):
        self.modelo = modelo
        self.cor = cor
        self.tampada = tampada

    def escrevendo(self):
        if self.tampada is True:
            print("A caneta está tampada.")
        else:
            print("Estou escrevendo")

    def com_tampa(self):
        self.tampada = True

    def sem_tampa(self):
        self.tampada = False

    def __str__(self):
        return f"Modelo: {self.modelo} - Cor: {self.cor} - Tampada: {self.tampada}."