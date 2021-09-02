from context import Instagram
import time
import csv
import requests

instagram = Instagram()

instagram_names = []
i = 0
with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)

    for row in csvReader:
        instagram_names.append(row[1])

    for account in instagram_names:
        print(account)
        medias = instagram.get_medias(account.strip(), 5)
        # Optional print to see the URL
        # print(medias[0].image_high_resolution_url)

        url = (str(medias[0].image_high_resolution_url))
        r = requests.get(url, allow_redirects=True)
        open(account + '_image.jpg', 'wb').write(r.content)
        print(r.headers.get('content-type'))

        url1 = (str(medias[1].image_high_resolution_url))
        r = requests.get(url1, allow_redirects=True)
        open(account + '_image1.jpg', 'wb').write(r.content)
        print(r.headers.get('content-type'))

        url2 = (str(medias[2].image_high_resolution_url))
        r = requests.get(url2, allow_redirects=True)
        open(account + '_image2.jpg', 'wb').write(r.content)
        print(r.headers.get('content-type'))

        url3 = (str(medias[3].image_high_resolution_url))
        r = requests.get(url3, allow_redirects=True)
        open(account + '_image3.jpg', 'wb').write(r.content)
        print(r.headers.get('content-type'))

        url4 = (str(medias[4].image_high_resolution_url))
        r = requests.get(url4, allow_redirects=True)
        open(account + '_image4.jpg', 'wb').write(r.content)
        print(r.headers.get('content-type'))

        time.sleep(60)
# Downloads in current directory
