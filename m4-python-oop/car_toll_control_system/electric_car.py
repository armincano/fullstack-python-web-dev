from vehicle import Vehicle


class ElectricCar(Vehicle):
    def __init__(
        self,
        brand: str,
        model: str,
        wheels_number: int,
        speed: int,
        motor_power: int,
        range: int,
        battery_capacity: float,
    ):
        super().__init__(brand, model, wheels_number)
        self.__speed = speed
        self.__motor_power = motor_power
        self.__range = range
        self.__battery_capacity = battery_capacity

    def __str__(self):
        return f"{super().__str__()}, Speed: {self.__speed} km/h, Motor power: {self.__motor_power} kw, Range: {self.__range} kms, Battery capacity: {self.__battery_capacity} kwh"

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def motor_power(self):
        return self.__motor_power
    @motor_power.setter
    def motor_power(self, motor_power):
        self.__motor_power = motor_power

    @property
    def range(self):
        return self.__range
    @range.setter
    def range(self, range):
        self.__range = range

    @property
    def battery_capacity(self):
        return self.__battery_capacity
    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity


class CargoCar(ElectricCar):
    def __init__(
        self,
        brand: str,
        model: str,
        wheels_number: int,
        speed: int,
        motor_power: int,
        range: int,
        battery_capacity: float,
        load_weight: float,
    ):
        super().__init__(
            brand, model, wheels_number, speed, motor_power, range, battery_capacity
        )
        self.__load_weight = load_weight

    def __str__(self):
        return f"{super().__str__()}, Load weight: {self.__load_weight} kgs"
    
    @property
    def load_weight(self):
        return self.__load_weight
    @load_weight.setter
    def load_weight(self, load_weight):
        self.__load_weight = load_weight

    @classmethod
    def tesla_cybertruck(cls):
        return cls(
            brand="Tesla",
            model="Cybertruck",
            wheels_number=6,
            speed=200,
            motor_power=800,
            range=800,
            battery_capacity=200,
            load_weight=1500,
        )


class PersonalCar(ElectricCar):
    def __init__(
        self,
        brand: str,
        model: str,
        wheels_number: int,
        speed: int,
        motor_power: int,
        range: int,
        battery_capacity: float,
        seats: int,
    ):
        super().__init__(
            brand, model, wheels_number, speed, motor_power, range, battery_capacity
        )
        self.__seats = seats

    def __str__(self):
        return f"{super().__str__()}, Seats number: {self.__seats}"
    
    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def seats(self, seats):
        self.__seats = seats

    @classmethod
    def tesla_model_s_plaid(cls):
        return cls(
            brand="Tesla",
            model="Model S Plaid",
            wheels_number=4,
            speed=250,
            motor_power=750,
            range=637,
            battery_capacity=100,
            seats=5,
        )

    @classmethod
    def byd_han(cls):
        return cls(
            brand="BYD",
            model="Han",
            wheels_number=4,
            speed=180,
            motor_power=363,
            range=605,
            battery_capacity=85.4,
            seats=5,
        )
