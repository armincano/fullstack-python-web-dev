from vehicle import Vehicle
from electric_car import ElectricCar, CargoCar, PersonalCar
from bicycle import Bicycle, Motorcycle
from utils.file_manager import CsvFileManager
from utils.create_custom_electric_car import create_custom_electric_car
from utils.generic_class import GenericClass

divider = ">>>--->>----------------------------------------\n"
vehicle_csv = "files/car_toll_control_system/vehicles.csv"


def main():
    """
    Brand: Ford
    Model: Mustang Mach-E
    Wheels Number: 4
    Speed: 200 km/h
    Motor Power: Up to 358 kW
    Range: 502 km
    Battery Capacity: 98.8 kWh
    """
    car_ford_mustang_mach_e = create_custom_electric_car(ElectricCar)
    print(car_ford_mustang_mach_e.__str__())
    personal = PersonalCar.tesla_model_s_plaid()
    personal_2 = PersonalCar.byd_han()
    cargo = CargoCar.tesla_cybertruck()
    bicycle = Bicycle.shimano_mt_ranger()
    motorcycle = Motorcycle.yamaha_mt07()
    test1 = GenericClass(attr1='value1', attr2='value2')
    test2 = "test"
    vehicle_instances = [test1, test2, personal, personal_2, cargo, bicycle, motorcycle]
    for vehicle in vehicle_instances:
        print(vehicle.__str__())

    print(f"\n{divider}")
    vehicle_classes = [Vehicle, ElectricCar, PersonalCar, CargoCar, Bicycle, Motorcycle]
    for vehicle_class in vehicle_classes:
        is_instance = f"Is {motorcycle.__class__} an instance of {vehicle_class.__name__}? {isinstance(motorcycle, vehicle_class)}"
        print(is_instance)

    csv_manager = CsvFileManager(vehicle_csv)
    csv_manager.write_csv(vehicle_instances, Vehicle)
    csv_manager.read_csv()
    
    print(f"\n{divider}")
    print(f"The brand for 'personal_2' instance is '{personal_2.brand}'")
    print("Change the brand of 'personal_2' instance using the setter method")
    personal_2.brand = "BYDXYZ"
    print(f"The brand for 'personal_2' instance is '{personal_2.brand}'")


if __name__ == "__main__":
    main()
