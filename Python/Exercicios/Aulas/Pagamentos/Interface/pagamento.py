from abc import ABC, abstractmethod

class PagamentoInterface(ABC):
    @abstractmethod
    def quitarPedido(self) -> str:
        pass