def input_string(message, min_length=1):
    while True:
        try:
            user_input = str(input(message))
            if len(user_input) < min_length:
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def input_int(message, min_value=0, max_value=10000):
    while True:
        try:
            user_input = int(input(message))
            if user_input < min_value:
                raise ValueError
            if user_input > max_value:
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid range. Please try again.")

def input_float(message, min_value=0, max_value=10000):
    while True:
        try:
            user_input = float(input(message))
            if user_input < min_value:
                raise ValueError
            if user_input > max_value:
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid range. Please try again.")
