import json
from cadastro import Cadastro

class FelipeBank:
    dados_cadastro = Cadastro
    def __init__(self):
        self.contas_cadastradas = []

    def abrir_conta(self, dados_cadastro):
        self.contas_cadastradas.append(dados_cadastro)
        # FelipeBank.__str__(self)
    
    def validar_senha(self, inf, senha):
        for i in range(len(self.contas_cadastradas)):
            aux = self.contas_cadastradas[i].dados
            if aux.get("numero_conta") == inf and aux.get("senha_conta") == senha:
                return True
        else:
            return False

    def emitir_extrato(self):
        inf = int(input("Informe o nº da conta: "))

        # Validar a senha da conta
        while True:
            senha = str(input("Senha da conta: "))
            b = self.validar_senha(inf, senha)
            if b == True:
                break
            else:
                return print("Senha errada ou conta inexistente!")

        for i in range(len(self.contas_cadastradas)):
            aux = self.contas_cadastradas[i].dados
            if aux.get("numero_conta") == inf:
                print(f"|---------------|\n Conta: {aux.get('numero_conta')} \n Situaçao: {aux.get('situacao_conta')} \n Saldo: R$ {aux.get('saldo_conta')} \n|---------------|")
                return

    def sacar_valor(self):
        inf = int(input("Informe o nº da conta: "))
        
        # Validar a senha da conta
        while True:
            senha = str(input("Senha da conta: "))
            b = self.validar_senha(inf, senha)
            if b == True:
                break
            else:
                return print("Senha errada ou conta inexistente!")

        for i in range(len(self.contas_cadastradas)):
            aux = self.contas_cadastradas[i].dados
            
            if aux.get("numero_conta") == inf:
                print(f"Saldo atual: {aux.get('saldo_conta')}")
                
                saque = float(input("Valor a ser sacado: "))
                
                if aux.get('saldo_conta') >= saque:
                    aux['saldo_conta'] = aux.get('saldo_conta') - saque
                else:
                    print("Você não tem saldo suficinete!")
                
                op = str(input("Saldo (S/n): "))
                
                if op in "Ss":
                    return self.emitir_extrato()
                else:
                    return

    def depositar_valor(self):
        inf = int(input("Informe o nº da conta: "))

        for i in range(len(self.contas_cadastradas)):
            aux = self.contas_cadastradas[i].dados
            
            if aux.get("numero_conta") == inf:
                print(f"Saldo atual: {aux.get('saldo_conta')}")
                
                deposito = float(input("Valor a ser depositado: "))
                
                aux['saldo_conta'] = aux.get('saldo_conta') + deposito
                
                op = str(input("Saldo (S/n): "))
                
                if op in "Ss":
                    return self.emitir_extrato()
                else:
                    return    
        else:
            print("Conta não existe!")
            return

    def encerrar_conta(self):
        inf = int(input("Informe o nº da conta: "))

        # Validar a senha da conta
        while True:
            senha = str(input("Senha da conta: "))
            b = self.validar_senha(inf, senha)
            if b == True:
                break
            else:
                return print("Senha errada ou conta inexistente!")

        for i in range(len(self.contas_cadastradas)):
            aux = self.contas_cadastradas[i].dados
            if aux.get("numero_conta") == inf:
                aux["situacao_conta"] = False
                return print("Sua conta foi encerrada")

    def __str__(self): # Visualizar o Banco
        print("Estado atual do FelipeBank: ")
        
        for i in range(len(self.contas_cadastradas)):
            print(json.dumps(self.contas_cadastradas[i].dados, sort_keys=False, indent=4))
        