from context import Instagram
from time import sleep
import pandas
import csv

instagram = Instagram()

# Created an array to store each instagram account.
instagram_account = []

# Used for the while loop.
i = 0

medias = instagram.get_medias('medicalskinaesthetics')

# Adding the instagram.csv file to the array (instagram_account)
with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        instagram_account.append(row[1])

# While loop for printing the instagram.csv account names.
while i < len(instagram_account):
    print(instagram_account[i])
    i += 1

media = medias[0]
media1 = medias[1]
media2 = medias[2]
media3 = medias[3]
media4 = medias[4]
print(media, media1, media2, media3, media4)
