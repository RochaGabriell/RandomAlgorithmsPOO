from employment import Employment

class Person:
    id: int
    name: str
    email: str
    employment: Employment

    def __init__(self, id: int, name: str, email: str, employment: Employment):
        self.id = id
        self.name = name
        self.email = email
        self.employment = employment