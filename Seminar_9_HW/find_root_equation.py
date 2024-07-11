import csv
import json
import random
import math


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            numbers = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(numbers)


def save_to_json(func):
    def wrapper(file_name):
        results = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(file_name)
                results.append({
                    "a": a,
                    "b": b,
                    "c": c,
                    "roots": roots
                })

        with open('results.json', mode='w') as json_file:
            json.dump(results, json_file, indent=4)

    return wrapper


@save_to_json
def find_roots(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = map(int, row)
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 101)
