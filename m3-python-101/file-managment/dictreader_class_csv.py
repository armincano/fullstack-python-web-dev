import csv
greats_quotes = "files/file_managment/small_greats_quotes_90.csv"
ghibli_characters_no_header = "files/file_managment/small_ghibli_characters_no_header.csv"
divider=">>>--->>----------------------------------------"

# without 'fieldnames' parameter, because the csv file has a header
with open(greats_quotes, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row['authors'])
        print(divider)

# with 'fieldnames' parameter, because the csv file has no header
with open(ghibli_characters_no_header, newline='') as csvfile:
    fieldnames = ['character', 'movie', 'release_date']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row)
        print(row['character'], row['movie'])