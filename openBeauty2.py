from context import Instagram
import time
import csv

instagram = Instagram()

instagram_names = []

with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)

    for row in csvReader:
        instagram_names.append(row[1])

    for account in instagram_names:
        print(account)
        medias = instagram.get_medias(account.strip(), 2)
        print(medias[0])
        time.sleep(30)
