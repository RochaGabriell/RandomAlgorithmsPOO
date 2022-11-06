from typing import Type
from interfaces.formas import FormasInterface

class Engenheiro():
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def calcularPerimetro(self, terreno: Type[FormasInterface]) -> None:
        perimetro = terreno.getPerimetro()
        print(f"{self.nome} está calculando o perimetro, deu {perimetro} m.")

    def calcularArea(self, terreno: Type[FormasInterface]) -> None:
        area = terreno.getArea()
        print(f"{self.nome} está calculando o perimetro, deu {area} m².")

