from context import Instagram
from time import sleep
import csv

proxies = {
    'http': 'http://150.239.66.202:3128',
    'https': 'http://185.8.2.132:3128',
}
instagram = Instagram()
instagram.set_proxies(proxies)

instagram_names = []
i = 0
with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)

    for row in csvReader:
        instagram_names.append(row[1])

    for account in instagram_names:
        print(account)
        medias = instagram.get_medias(account.strip(), 2)
        print(medias)
