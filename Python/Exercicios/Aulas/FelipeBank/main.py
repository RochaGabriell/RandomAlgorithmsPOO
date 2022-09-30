from banco import FelipeBank 
from cadastro import Cadastro

def main():
    banco = FelipeBank()

    numero_conta = [101, 102, 103]
    abertura_conta = ["01/05/2022", "19/07/2022", "28/08/2022"]
    fechamento_conta = ["01/05/2026", "19/07/2026", "28/08/2026"]
    situacao_conta = [True, True, True]
    senha_conta =[123, 321, 432]
    saldo_conta = [11, 2, 1234]

    for i in range(len(numero_conta)):
        banco.abrir_conta(Cadastro(numero_conta[i], abertura_conta[i], fechamento_conta[i], situacao_conta[i], senha_conta[i], saldo_conta[i]))

    banco.sacar_valor()

    banco.emitir_extrato()

    banco.depositar_valor()
    
    banco.encerrar_conta()

    banco.estado_banco()

if __name__ == "__main__": # Executar o código apenas se o arquivo foi executado diretamente e não importado
    main()