from context import Instagram
import time
import csv
import requests

instagram = Instagram()
instagram_names = []
with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)

    for row in csvReader:
        instagram_names.append(row[1])

    for account in instagram_names:
        print(account)
        i = 0
        medias = instagram.get_medias(account.strip(), 5)
        # Optional print to see the URL
        # print(medias[0].image_high_resolution_url)
        while i < 5:
            # Downloads first URL
            url = (str(medias[i].image_high_resolution_url))
            r = requests.get(url, allow_redirects=True)
            open(account + '_image' + str(i) + '.jpg', 'wb').write(r.content)
            print(r.headers.get('content-type'))
            i += 1

        time.sleep(60)
# Downloads in current directory
