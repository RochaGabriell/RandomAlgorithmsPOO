from person import Person

class Teacher(Person):
    def __init__(self, fname: str, lname: str, cpf: int, siape: str):
        super().__init__(fname, lname, cpf)
        self.siape = siape

    def print_DadosT(self):
        print(self.firstname, self.siape)