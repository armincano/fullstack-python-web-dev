from vehicle import Vehicle


class Bicycle(Vehicle):
    def __init__(self, brand: str, model: str, wheels_number: int, type: str):
        super().__init__(brand, model, wheels_number)
        self.__type = type

    def __str__(self):
        return f"{super().__str__()}, Type: {self.__type}"
    
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type = type

    @classmethod
    def shimano_mt_ranger(cls):
        return cls(brand="Shimano", model="MT Ranger", wheels_number=2, type="Racing")


class Motorcycle(Bicycle):
    def __init__(
        self,
        brand: str,
        model: str,
        wheels_number: int,
        type: str,
        spokes_number: int,
        frame: str,
        engine: str,
    ):
        super().__init__(brand, model, wheels_number, type)
        self.__spokes_number = spokes_number
        self.__frame = frame
        self.__engine = engine

    def __str__(self):
        return f"{super().__str__()}, Spokes: {self.__spokes_number}, Frame: {self.__frame}, Engine: {self.__engine}"
    
    @property
    def spokes_number(self):
        return self.__spokes_number
    @spokes_number.setter
    def spokes_number(self, spokes_number):
        self.__spokes_number = spokes_number
    
    @property
    def frame(self):
        return self.__frame
    @frame.setter
    def frame(self, frame):
        self.__frame = frame
        
    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @classmethod
    def yamaha_mt07(cls):
        return cls(
            brand="Yamaha",
            model="MT-07",
            wheels_number=2,
            type="Racing",
            spokes_number=36,
            frame="Aluminum",
            engine="689cc inline twin",
        )
