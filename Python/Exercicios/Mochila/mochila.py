from itens import Itens

class Mochila:
    tens = Itens
    def __init__(self, marca : str, cor : str, capacidade : int) -> None:
        self.limite = []
        self.marca = marca
        self.cor = cor
        self.capacidade = capacidade

    def colocar_mochila(self, tens):
        aux = 0
        for i in range(len(self.limite)):
            aux += self.limite[i].peso
        if aux + tens.peso <= self.capacidade:
            self.limite.append(tens)
            for i in range(len(self.limite)):
                print(self.limite[i].nome, self.limite[i].peso)
            print("Sim")
        else:
            print("Não")

    def __str__(self) -> str:
        print(f"A mochila {self.marca} da cor {self.cor} foi add.\nCapacidade: {self.capacidade}")