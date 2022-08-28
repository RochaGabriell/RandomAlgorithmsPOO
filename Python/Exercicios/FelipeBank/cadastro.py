class Cadastro:
    numero_conta : int
    abertura_conta : str
    fechamento_conta : str
    situacao_conta : bool
    senha_conta : str
    saldo_conta : float

    def __init__(self, numero_conta : int, abertura_conta : str, fechamento_conta : str, situacao_conta : bool, senha_conta : str, saldo_conta: float):
        #self.numero_conta = numero_conta # int
        #self.abertura_conta = abertura_conta # date
        #self.fechamento_conta = fechamento_conta # date
        #self.situacao_conta = situacao_conta # string
        #self.senha_conta = senha_conta # string
        #self.saldo_conta = saldo_conta # float
        self.dados = {
            "numero_conta" : int(numero_conta),
            "abertura_conta" : str(abertura_conta),
            "fechamento_conta" : str(fechamento_conta),
            "situacao_conta" : bool(situacao_conta),
            "senha_conta" : str(senha_conta),
            "saldo_conta" : float(saldo_conta)
        }
