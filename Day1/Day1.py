#Day 1 Puzzle - Return calorie count of Elf that has most snacks 

with open("data.txt", "r") as f:
    raw_data = f.read()

    raw_data_list = raw_data.split("\n")


record_calories = 0
current_calories = 0

for item in raw_data_list:
    if item == "":
        current_calories = 0
    else:
        current_calories += int(item)

    if current_calories > record_calories:
        record_calories = current_calories

print(f"Record = {record_calories}")

