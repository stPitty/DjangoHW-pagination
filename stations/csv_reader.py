import csv

def read_csv(file_path):
    result = []
    with open(file_path) as file:
        data = csv.DictReader(file)
        for row in data:
            result.append(row)
    return result
