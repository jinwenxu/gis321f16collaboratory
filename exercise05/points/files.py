import csv

def read_csv(file_name):
    newlines = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            newlines.append(line)
    return newlines