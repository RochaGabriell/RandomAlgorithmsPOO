class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def sentar(self):
        print(self.nome.title() + " sentar agora")
        
    def rolar(self):
        print(self.nome.title() + " rolar")
    
meu_cachorro = Dog("Osca", 3)

# Acessar uma determinada váriavel
print(f"Meu cachorro se chama {meu_cachorro.nome}, e tem {meu_cachorro.idade} anos.")

# Acessar um metodo
meu_cachorro.sentar()