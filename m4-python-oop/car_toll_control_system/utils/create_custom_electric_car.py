from utils.user_input_validation import input_string, input_int, input_float

def create_custom_electric_car(class_name):
    brand = input_string("Enter the car brand: ")
    model = input_string("Enter the car model: ")
    wheels_number = input_int("Enter the car wheels number: ")
    speed = input_int("Enter the car speed in km/h: ")
    motor_power = input_int("Enter the car motor power in kw: ")
    range = input_int("Enter the car range in km: ")
    battery_capacity = input_float("Enter the car battery capacity in kwh: ")
    return class_name(
        brand, model, wheels_number, speed, motor_power, range, battery_capacity
    )
