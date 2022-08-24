from xmlrpc.client import boolean
import caneta 

for i in range(2):
    modelo = str(input("Modelo -> "))
    cor = str(input("Cor -> "))
    tampa = str(input("Tampa (S/n) -> "))
    tampa = False if tampa not in "Ss" else True

    chambrada = caneta.Caneta(modelo, cor, tampa)
    chambrada.rabiscar()
    print(chambrada.__str__())