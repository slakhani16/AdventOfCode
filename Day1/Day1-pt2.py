#Day 1 Puzzle - Return calorie count of Top 3 Elves that have most snacks and return total

with open("data.txt", "r") as f:
    raw_data = f.read()

    raw_data_list = raw_data.split("\n")


number_of_top_records = 3
record_calories = []
current_calories = 0

for item in raw_data_list:
    if item == "":
        # Elf data complete
        if len(record_calories) < number_of_top_records:
            record_calories.append(current_calories)
            record_calories.sort()
            current_calories = 0
            continue
        
        record_calories_copy = record_calories.copy()

        for index, record in enumerate(record_calories):
            if current_calories > record:
                if index == 0:
                    record_calories_copy[0] = current_calories
                else:
                    record_calories_copy[index - 1] = record_calories_copy[index]
                    record_calories_copy[index] = current_calories

        record_calories = record_calories_copy

        current_calories = 0
    else:
        current_calories += int(item)

print(f"Record = {record_calories}")

