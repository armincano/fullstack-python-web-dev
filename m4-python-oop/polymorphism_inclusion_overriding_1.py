class Animal:
    def __init__(self, name: str, specie: str, breed: str, age: int, weight: float):
        self.name: str = name
        self.specie: str = specie
        self.breed: str = breed
        self.age: int = age
        self.weight: float = weight

    def __str__(self):
        return f"✎﹏﹏﹏﹏﹏﹏﹏﹏﹏\nName: {self.name}\nSpecie: {self.specie}\nBreed: {self.breed}\nAge: {self.age}\nWeight: {self.weight}\n﹏﹏﹏﹏﹏﹏﹏﹏﹏₊∘"

    def eat(self):
        print(f"{self.name} is eating")
        
    def walk(self):
        print(f"{self.name} is walking")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def __init__(self, name: str, breed: str, age: int, weight: float):
        super().__init__(name, "Dog", breed, age, weight)
        
    def walk(self):
        print(f"{self.name} is walking like a dog")
        
class Cat(Animal):
    def __init__(self, name: str, breed: str, age: int, weight: float):
        super().__init__(name, "Cat", breed, age, weight)
        
    def walk(self):
        print(f"{self.name} is walking like a cat")


dog_brando = Dog("Brando","San Bernardo", 3, 30)
cat_roll = Cat("Roll","Persa", 4, 3)

print(dog_brando.name)
print(dog_brando.age)
print(dog_brando.specie)
print(dog_brando.breed)
print(dog_brando.weight)
print(dog_brando.__str__())
dog_brando.walk()
dog_brando.eat()
cat_roll.walk()
cat_roll.eat()