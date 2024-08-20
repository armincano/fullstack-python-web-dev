user_age = None
while True:
    input_age = input("Write your age: ")
    try:
        user_age = int(input_age)
        break
    except ValueError:
        print("The input age must be a number. Please try again.")

is_adult = "You are an Adult" if user_age >= 18 else "You are not an Adult."
print(is_adult)
"""
1. Design a Python program that asks the user for their age via the console.
2. The user must enter an integer; otherwise, the program will throw an exception and ask the user to enter their age again.
3. Next, the program should print "Adult" if the age is 18 or older; otherwise, it should print "Not an adult."
"""