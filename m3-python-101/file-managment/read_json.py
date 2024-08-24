import json

apple_info = "files/json/apple-products-people.json"
json_output_file = "files/json/output.json"
divider_1 = ">>>--->>----------------------------------------"

with open(apple_info, "r") as infile:
    apple_info = json.load(infile)

for product in apple_info["products"]:
    name = product["name"]
    release_date = product["releaseDate"]
    print(f"{name} was released on {release_date}")

print(divider_1)

for person in apple_info["people"]:
    name = person["name"]
    role = person["role"]
    is_serving = "is" if person["yearsActive"].find("present") != -1 else "was"
    print(f"{name} {is_serving} {role}")

reduced_apple_people = {"people": []}
for person in apple_info["people"]:
    reduced_apple_people["people"].append(
        {"name": person["name"], "role": person["role"]}
    )

with open(json_output_file, "w") as outfile:
    json.dump(reduced_apple_people, outfile, indent=4)
