from Interface.pagamento import PagamentoInterface

class PagamentoCartaoCredito(PagamentoInterface):
    def quitarPedido(self) -> str:
        return "Pamento via Cartão de Credito!"