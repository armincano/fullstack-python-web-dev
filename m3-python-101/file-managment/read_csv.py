import csv

ghibli_characters_file_path = "files/file_managment/ghibli_characters.csv"
new_ghibli_characters_file_path = "files/file_managment/new_ghibli_characters.csv"
filtered_row_values = []

with open(ghibli_characters_file_path, mode="r") as infile:
    reader = csv.reader(infile)
    for value in reader:
        new_row = [value[0],value[7],value[8]]
        filtered_row_values.append(new_row)

with open(new_ghibli_characters_file_path, mode="w", newline="") as outfile:
    writer = csv.writer(outfile)
    for row in filtered_row_values:
        writer.writerow(row)

