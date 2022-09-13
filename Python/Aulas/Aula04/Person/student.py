from person import Person

class Student(Person):
    def __init__(self, fname: str, lname: str, cpf: int, matricula: str):
        super().__init__(fname, lname, cpf)
        self.matricula = matricula

    def print_Dados(self):
        print(self.firstname, self.matricula)