class Person:
    def __init__(
        self, name: str, surname: str, sex: str, age: int, height: float, weight: float
    ):
        self._name = name
        self._surname = surname
        self._sex = sex
        self._age = age
        self._height = height
        self._weight = weight

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
        
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        self._weight = value

    def __str__(self):
        return f"✎﹏﹏﹏﹏﹏﹏﹏﹏﹏\nNombre: {self.name}\nApellido: {self.surname}\nSexo: {self.sex}\nEdad: {self.age} años\nAltura: {self.height} mts\nMasa: {self.weight} kg\n﹏﹏﹏﹏﹏﹏﹏﹏﹏₊∘"

persona_1 = Person("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Person("Juan", "Camargo", "Masculino", 18, 1.8, 75)
print(persona_1.__str__())
print(persona_2.__str__())
print("Change the age of persona_1 and the surname of persona_2")
persona_1.age = 21
persona_2.surname = "Santiago"
print(persona_1.__str__())
print(persona_2.__str__())