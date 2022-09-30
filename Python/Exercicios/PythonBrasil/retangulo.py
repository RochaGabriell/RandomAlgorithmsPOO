class Retangulo:
    def __init__(self, ladoA: float, ladoB: float) -> None:
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValores(self, base: float, altura: float) -> None:
        self.ladoA = base
        self.ladoB = altura

    def valoreLados(self) -> str:
        return f"Base: {self.ladoA}; Altura: {self.ladoB}."

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return self.ladoA*2 + self.ladoB*2


retangulo = Retangulo(4, 10)
print(retangulo.valoreLados())
print(f"Área: {retangulo.calcularArea()}m²")
print(f"Perímetro: {retangulo.calcularPerimetro()}m²")

retangulo.mudarValores(5, 14)
print(retangulo.valoreLados())
print(f"Área: {retangulo.calcularArea()}m²")
print(f"Perímetro: {retangulo.calcularPerimetro()}m²")

print(f"{retangulo.calcularArea()}m² de piso e {retangulo.calcularPerimetro()}m² de rodapés para suprir o local.")