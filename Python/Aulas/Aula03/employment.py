class Employment:
    id: int
    charge: str
    start_time: str

    def __init__(self, id: int, charge: str, start_time: str):
        self.id = id
        self.charge = charge
        self.start_time = start_time