class Person:
    def __init__(self, fname: str, lname: str, cpf: int):
        self.firstname = fname
        self.lastname = lname
        self.cpf = cpf
    
    def print_Name(self):
        print(self.firstname, self.lastname, self.cpf)