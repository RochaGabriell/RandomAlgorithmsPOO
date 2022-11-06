from interfaces.formas import FormasInterface

class Retangulo(FormasInterface):
    def __init__(self, comprimento: int, largura: int) -> None:
        super().__init__()
        self.comprimento = comprimento
        self.largura = largura

    def getPerimetro(self) -> int:
        print("Perimetro - Retangulo:")
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro

    def getArea(self) -> int:
        print("Área - Retangulo:")
        area = self.comprimento * self.largura
        return area