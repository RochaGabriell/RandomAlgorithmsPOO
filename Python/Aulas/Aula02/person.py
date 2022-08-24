class Person:
  def __init__(self, name, age, phone):
    self.name = name
    self.age = age
    self.phone = phone

  def myfunc(self):
    print(f"Olá! Meu nome é {self.name}, tenho {self.age}.")

# p1 = Person("Gabriel Rocha", 18, "(89) 98127-4201")
# p1.myfunc()

lista = []

for i in range(2):
  nome = input("-> ")
  idade = int(input("-> "))
  telefone = input("-> ")
  lista.append(Person(nome, idade, telefone))

for i, j in enumerate(lista):
  print(f"{i} - {j.name, j.age, j.phone}")
