class  Person:
    def __init__(self, name="Person", age=0):
        self.name = name
        self.age = age

class Hero(Person):
    def __init__(self, name, age, superpower):
        super().__init__(name, age)
        self.superpower = superpower

    def display_info(self):
        print(f"Hero Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Superpower: {self.superpower}")

hero = Hero("Nickgrr", 30, "Super Strength")
hero.display_info()
