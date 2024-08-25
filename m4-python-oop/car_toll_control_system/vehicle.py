class Vehicle:
    def __init__(self, brand: str, model: str, wheels_number: int):
        self.__brand = brand
        self.__model = model
        self.__wheels_number = wheels_number
    
    def __str__(self):
        divider = ">>>---------------------------------------------\n"
        return f"{divider}Brand: {self.__brand}, Model: {self.__model}, {self.__wheels_number} wheels"
    
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand
    
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model
    
    @property
    def wheels_number(self):
        return self.__wheels_number
    @wheels_number.setter
    def wheels_number(self, wheels_number):
        self.__wheels_number = wheels_number