class Product:
    def __init__(self, name:str, price:int, stock:int):
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        try:
            if value < 0:
                raise ValueError(f"You entered {value}, but Price cannot be negative")
            self.__price = value
        except ValueError as error:
            print(error)
    
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, value):
        try:
            if value < 0:
                raise ValueError(f"You entered {value}, but Stock cannot be negative")
            self.__stock = value
        except ValueError as error:
            print(error)
            
""" product_1=Product("Laptop", 1000, 10)
product_1.price = -1
product_1.price = 500
print(product_1.price) """