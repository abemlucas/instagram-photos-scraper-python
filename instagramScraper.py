from context import Instagram
import time
import csv
import requests

instagram = Instagram()

# Array to store the instagram accounts

# Opens the csv file where the Instagram accounts are stored

with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)

    for row in csvReader:
        print(row[1])
        i = 0
        medias = instagram.get_medias(row[1].strip(), 5)

        # Optional print to see the URL
        # print(medias[0].image_high_resolution_url)
        for posts in medias:

            # Downloads URL as high resolution image regardless of type.
            url = str(posts.image_high_resolution_url)
            responses = requests.get(url, allow_redirects=True)
            open('images/'+row[1] + '_image' + str(i) +
                 '.jpg', 'wb').write(responses.content)
            i += 1

        time.sleep(60)
# Downloads in current directory
