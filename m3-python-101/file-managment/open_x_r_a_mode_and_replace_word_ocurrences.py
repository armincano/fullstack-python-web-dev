file_path = "files/informacion.dat"

def print_file(file_path):
    try:
        with open(file_path, "r") as infile:
            for line in infile:
                print(line, end="")
    except FileNotFoundError:
        print("El archivo informacion.dat no se encuentra en la ruta especificada")
        print(">>>--->>----------------------------------------")

def create_file_with_content(file_path):
    try:
        with open(file_path, "x") as outfile:
            print(f"The file was created at {file_path}")
            for row_line in range(1, 6):
                row_string = f"Datos de información en la línea {row_line}"
                outfile.write(f"{row_string}\n")
    except FileExistsError:
        print("El archivo informacion.dat ya existe, ha sido creado previamente")
        print(">>>--->>----------------------------------------")

def append_content_to_file(file_path):
    try:
        text_to_add = ["Hola Mundo", "Este en una nueva línea en el archivo", "agregando la segunda línea del archivo", "finalizando la línea agregada"]
        with open(file_path, "a") as outfile:
            for row in text_to_add:
                outfile.write(row+"\n")
    except FileNotFoundError:
        print("El archivo informacion.dat no se encuentra en la ruta especificada")
    finally:
        print_file(file_path)
        print(">>>--->>----------------------------------------")

def replace_word_ocurrences(file_path):
    old_word = "información"
    new_word = "procesamiento"
    try:
        with open(file_path, "r") as infile:
            lines = infile.readlines()
        with open(file_path, "w") as outfile:
            for line in lines:
                outfile.write(line.replace(old_word, new_word))
    except FileNotFoundError:
        print("El archivo informacion.dat no se encuentra en la ruta especificada")
    finally:
        print_file(file_path)
        print(">>>--->>----------------------------------------")

create_file_with_content(file_path)
append_content_to_file(file_path)
replace_word_ocurrences(file_path)