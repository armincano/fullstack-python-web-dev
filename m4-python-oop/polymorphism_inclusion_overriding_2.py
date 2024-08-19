class Person:
    def __init__(self, name: str):
        self.name = name
        
    def movement(self):
        print(f"{self.name} is walking")
        
class Marathoner(Person):
    def __init__(self, name: str):
        super().__init__(name)
        
    def movement(self):
        print(f"{self.name} is trotting")

class Cyclist(Person):
    def __init__(self, name: str):
        super().__init__(name)
        
    def movement(self):
        print(f"{self.name} is rolling")
        
person_1 = Person("Jose")
marathoner_1 = Marathoner("Moisés")
cyclist_1 = Cyclist("César")

person_1.movement()
marathoner_1.movement()
cyclist_1.movement()