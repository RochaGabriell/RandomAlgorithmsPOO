class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name
    
    def __format__(self, __format_spec: str) -> str:
        if __format_spec == "scream":
            return self.name.upper() + "!"
        elif __format_spec == "repeat":
            return self.name * 3
        return self.name
    
person = Person("Gabriel")

print(f"{person}")
print(f"{person:scream}")
print(f"{person:repeat}")