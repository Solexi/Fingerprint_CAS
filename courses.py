import csv

with open('courses.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"('{row[0]}', '{row[1]}', '{row[2]}'),")