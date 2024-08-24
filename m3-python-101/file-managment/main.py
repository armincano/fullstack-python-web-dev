import os
from todo_manager import TodoManager

umineko_file_path = "files/file_managment/umineko.txt"
todo_file_path = "files/file_managment/tasks_1.txt"
copy_file_path = "files/file_managment/copy_tasks.txt"
replace_file_path = "files/file_managment/replace_words_tasks.txt"
divider_1 = ">>>--->>----------------------------------------"
divider_2 = "----------------------------------------<<---<<<"

def clear():  # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        print(divider_2)
        print("M A I N   M E N U")
        print(
            "1 ➜ Read your tasks\n2 ➜ Add tasks\n3 ➜ Count lines\n4 ➜ Count words\n5 ➜ Replace character sequence occurrences and save to a new file\n6 ➜ Copy your tasks to a file\n7 ➜ Exit"
        )
        try:
            user_input = int(input("Write your option: "))
            match user_input:
                case 1:
                    clear()
                    todo.read_tasks()
                case 2:
                    clear()
                    todo.add_tasks()
                case 3:
                    clear()
                    todo.count_lines()
                case 4:
                    clear()
                    todo.count_words()
                case 5:
                    clear()
                    todo.replace_char_sequence_occurrences()
                case 6:
                    clear()
                    todo.copy_tasks_to_new_file()
                case 7:
                    break
                case _:
                    print("Not a valid option")
        except ValueError:
            print("You must enter a number.")

print(divider_1)
print("Hi! Welcome to your Todo manager ✔")
todo = TodoManager(todo_file_path, copy_file_path, replace_file_path)
if __name__ == "__main__":
    main()
