class ContaCorrente:
    def __init__(self, numeroConta: str, nomeCorrentista: str, saldo: float = 0) -> None:
        self.__numeroConta = numeroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

    def __validarConta(self, numConta: str) -> bool:
        if self.__numeroConta == numConta:
            return True
        return False
    
    def __validarSaldo(self, valor: float) -> bool:
        if self.__saldo >= valor:
            return True
        return False

    @property
    def nomeCorrentista(self) -> str:
        return self.__nomeCorrentista

    def alterarNome(self, numeroConta: str, nome_novo) -> None:
        if self.__validarConta(numeroConta):
            self.__nomeCorrentista = nome_novo
            return
        return False

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def depositar(self, valor: float) -> None:
        self.__saldo += valor
    
    def saque(self, valor: float, numConta: str) -> bool:
        if self.__validarConta(numConta) and self.__validarSaldo(valor):
            self.__saldo -= valor
            return True
        return False

conta = ContaCorrente("0019", "Gabriel Rocha")

conta.depositar = 100
print(conta.saldo)

print("Valor sacado") if conta.saque(100, "0019") else print("Erro")

print(conta.saldo)

print("Nome mudado") if conta.alterarNome("0019", "Gabriel Silva") == None else print("Conta errada ou não existe")
