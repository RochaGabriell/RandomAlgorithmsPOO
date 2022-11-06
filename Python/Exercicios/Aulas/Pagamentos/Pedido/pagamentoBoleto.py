from Interface.pagamento import PagamentoInterface

class PagamentoBoleto(PagamentoInterface):
    def quitarPedido(self) -> str:
        return "Pamento via boleto!"