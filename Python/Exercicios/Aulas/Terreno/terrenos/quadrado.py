from interfaces.formas import FormasInterface

class Quadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        super().__init__()
        self.lado = lado

    def getPerimetro(self) -> int:
        print("Perimetro - Quadrado:")
        perimetro = self.lado * 4
        return perimetro

    def getArea(self) -> int:
        print("Área - Quadrado:")
        area = self.lado * self.lado
        return area