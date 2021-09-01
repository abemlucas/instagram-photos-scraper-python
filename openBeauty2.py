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
        medias = instagram.get_medias(account.strip(), 5)
        print(medias[0], medias[1], medias[2], medias[3], medias[4])
        time.sleep(60)
