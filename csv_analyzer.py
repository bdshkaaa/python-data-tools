import csv
from collections import Counter


def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def analyze_column(data, column_name):
    values = [row[column_name] for row in data if column_name in row]
    counter = Counter(values)
    return counter


def print_report(counter):
    print("Value counts:\n")
    for value, count in counter.items():
        print(f"{value}: {count}")


def main():
    file_path = "data.csv"
    column_name = "category"

    data = read_csv(file_path)
    counter = analyze_column(data, column_name)
    print_report(counter)


if __name__ == "__main__":
    main()