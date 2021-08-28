from context import Instagram
from time import sleep
import csv

instagram = Instagram()

instagram_names = []
i = 0
with open('test.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)

    for row in csvReader:
        instagram_names.append(row[1])

while i < len(instagram_names):

    print(instagram_names[i])
    medias = instagram.get_medias(str(instagram_names[i]))
    media = medias[0]
    media1 = medias[1]
    media2 = medias[2]
    media3 = medias[3]
    media4 = medias[4]
    print(media, media1, media2, media3, media4)
    i += 1
