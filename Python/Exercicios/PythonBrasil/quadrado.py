class Quadrado:
    def __init__(self, tamanhoLado: float) -> None:
        self.tamanhoLado = tamanhoLado

    def mudarValor(self, novo_valor: float) -> None:
        self.tamanhoLado = novo_valor

    def retornaValor(self) -> float:
        return self.tamanhoLado

    def calcularArea(self) -> float:
        return f"Quadrado com lado {self.tamanhoLado} tem área igual {self.tamanhoLado**2}."

quadrado = Quadrado(20)
print(quadrado.retornaValor())
quadrado.mudarValor(30)
print(quadrado.calcularArea())