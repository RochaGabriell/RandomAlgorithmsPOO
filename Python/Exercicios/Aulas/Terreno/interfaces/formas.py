from abc import ABC, abstractmethod

class FormasInterface(ABC):
    @abstractmethod
    def getPerimetro(self) -> int:
        pass

    @abstractmethod
    def getArea(self) -> int:
        pass