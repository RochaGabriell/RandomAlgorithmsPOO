from person import Person
from employment import Employment

def main():
    e = Employment(1, "Professor", "18h")
    p = Person(1, "Felipe", "fds@gmail.com", e)

    print(p.name, p.employment.charge)

if __name__ == "__main__":
    main()