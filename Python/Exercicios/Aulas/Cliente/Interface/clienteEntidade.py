from abc import ABC, abstractmethod
from datetime import datetime

class ClienteEntidadeInterface(ABC):
    def __init__(self, identificador: int, nome: str, dataNascimento: datetime, status: bool) -> None:
        self.identificador = identificador
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.status = status