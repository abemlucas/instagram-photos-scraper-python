import csv

names = []

i = 0

with open('test.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        names.append(row[0])

while i < len(names):
    print(names[i])
    i += 1
