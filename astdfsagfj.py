class Prisoner:
    def __init__(self, name, crime):
        self.name = name
        self.crime = crime


class CopCar:
    def __init__(self, model):
        self.model = model
        self.prisoners = []

    def add_prisoner(self, prisoner):
        self.prisoners.append(prisoner)

    def print_prisoners_info(self):
        if self.prisoners:
            print(f"Prisoners in the {self.model}:")
            for prisoner in self.prisoners:
                print(f"{prisoner.name}: {prisoner.crime}")
        else:
            print(f"There are no prisoners in the {self.model}")


prisoner1 = Prisoner("Murad bagirzade", "nadoel uzhe")
prisoner2 = Prisoner("Poop eater", "etinq poop")
cop_car = CopCar("nigger machine")
cop_car.add_prisoner(prisoner1)
cop_car.add_prisoner(prisoner2)
cop_car.print_prisoners_info()
