import csv
import ast

class CsvFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                vehicles_list = [row for row in reader]
                vehicles_dict = {"PersonalCar": [], "CargoCar": [], "ElectricCar": [], "Bicycle": [], "Motorcycle": []}
                for vehicle in vehicles_list:
                    try:
                        if vehicle[0].find("PersonalCar") != -1:
                            vehicles_dict["PersonalCar"].append(ast.literal_eval(vehicle[1]))
                        elif vehicle[0].find("CargoCar") != -1:
                            vehicles_dict["CargoCar"].append(ast.literal_eval(vehicle[1]))
                        elif vehicle[0].find("ElectricCar") != -1:
                            vehicles_dict["ElectricCar"].append(ast.literal_eval(vehicle[1]))
                        elif vehicle[0].find("Bicycle") != -1:
                            vehicles_dict["Bicycle"].append(ast.literal_eval(vehicle[1]))
                        elif vehicle[0].find("Motorcycle") != -1:
                            vehicles_dict["Motorcycle"].append(ast.literal_eval(vehicle[1]))
                        else:
                            raise ValueError(f"Invalid vehicle class: {vehicle[0]}")
                    except ValueError as e:
                        self.print_warning(e)
                        continue
                for instance, vehicles in vehicles_dict.items():
                    self.print_divider()
                    print(f"List of {instance} vehicles:")
                    for instance in vehicles:
                        print(f"➜ {instance}")
        except FileNotFoundError:
            print("File not found.")

    def write_csv(self, vehicle_instances:list, valid_parent_class):
        try:
            with open(self.file_path, 'w') as outfile:
                writer = csv.writer(outfile)
                for instance in vehicle_instances:
                    try:
                        if not isinstance(instance, valid_parent_class):
                            raise ValueError(f"Invalid instance type. Expected {valid_parent_class.__name__} but got {instance.__class__.__name__}.\nThis element will be skipped. The process continue.")
                        data = [(instance.__class__,instance.__dict__)]
                        writer.writerows(data)
                    except ValueError as e:
                        self.print_warning(e)
                        continue
        except FileNotFoundError:
            print("File not found.")
    
    @staticmethod
    def print_divider():
        divider = "\n>>>--->>----------------------------------------"
        print(divider)
    
    @staticmethod
    def print_warning(error="error"):
        divider = "\n>>>--->>----------------------------------------"
        danger_string = "⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠"
        print(divider)
        print(error)
        print(danger_string)