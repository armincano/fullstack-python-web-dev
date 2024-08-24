import os
import re


class TodoManager:
    def __init__(self, file_path, copy_file_path, replace_words_file_path):
        self.__file_path = file_path
        self.__copy_file_path = copy_file_path
        self.__replace_words_file_path = replace_words_file_path

    @staticmethod
    def clear():  # Clear the terminal screen
        os.system("cls" if os.name == "nt" else "clear")

    def read_tasks(self):
        try:
            with open(self.__file_path, "r") as file:
                content = file.read()
                if len(content) == 0:
                    print("Your file is empty")
                else:
                    for idx, row in enumerate(content.splitlines()):
                        print(f"task {idx+1}: '{row}'")
        except FileNotFoundError:
            print("The file was not found.")

    def add_tasks(self):
        tasks = []
        print("Write 1, 2 or a new task.")
        print("1 ➜ save your tasks and exit.\n2 ➜ discard changes and exit.")
        while True:
            new_task = input("✎﹏")
            if new_task == "2":
                break
            elif new_task == "1":
                for task in tasks:
                    with open(self.__file_path, "a") as file:
                        file.write(f"{task}\n")
                self.clear()
                break
            else:
                tasks.append(new_task)
                print("✔")

    def count_lines(self):
        try:
            with open(self.__file_path, "r") as file:
                content = file.read()
                line_counter = 0
                for row in content.splitlines():
                    line_counter += 1
                print(f"This file have {line_counter} lines.")
        except FileNotFoundError:
            print("The file was not found.")

    def count_words(self):
        try:
            with open(self.__file_path, "r") as file:
                content = file.read()
                words = re.findall(r"\b\w+\b", content)
                words_counter = len(words)
            print(f"This file have {words_counter} words.")
        except FileNotFoundError:
            print("The file was not found.")

    def replace_char_sequence_occurrences(self):
        self.read_tasks()
        divider_1 = ">>>--->>----------------------------------------"
        print(divider_1)
        try:
            content = None
            modified_content = None
            with open(self.__file_path, "r") as infile:
                content = infile.read()

            old_word = input(
                "From your tasks, which sequence of characters do you want to replace: "
            )
            new_word = input("Write the sequence to use as replacement: ")
            print(divider_1)
            
            modified_content = content.replace(old_word, new_word)
            if modified_content == content:
                print(f"Word '{old_word}' was not found in the tasks.")
                return
            
            print("Do you want to apply the replacement?")
            print("1 ➜ apply.\n2 ➜ discard and exit.")
            do_save = int(input("Write your option: "))
            if do_save != 1:
                return
            
            with open(self.__replace_words_file_path, "w") as outfile:
                outfile.write(modified_content)
                print(
                    f"Word '{old_word}' has been replaced by '{new_word}' in {self.__replace_words_file_path}."
                )
        except FileNotFoundError:
            print("The file was not found.")
        except ValueError:
            print("You must enter a number.")

    def copy_tasks_to_new_file(self):
        try:
            with open(self.__file_path, "r") as infile:
                tasks_content = infile.read()

            with open(self.__copy_file_path, "w") as outfile:
                outfile.write(tasks_content)
            print(f"Tasks have been copied to {self.__copy_file_path}.")
        except FileNotFoundError:
            print("There is no file to copy from.")
