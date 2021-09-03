from context import Instagram
import time
import csv
import requests

instagram = Instagram()

# Array to store the instagram accounts

instagram_names = []

# Opens the csv file where the Instagram accounts are stored

with open('instagram.csv') as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    header = next(csvReader)

    # Starts adding to the array from the second line of the instagram.csv file

    for row in csvReader:
        instagram_names.append(row[1])

    for account in instagram_names:
        print(account)

        i = 0
        medias = instagram.get_medias(account.strip(), 5)

        # Optional print to see the URL
        # print(medias[0].image_high_resolution_url)
        
        #Change the value of i to change the number of photos downloaded.
        while i < 5:

            # Downloads URL as high resolution image regardless of type.

            url = (str(medias[i].image_high_resolution_url))
            r = requests.get(url, allow_redirects=True)
            
            #Creat an 'images' folder in working directory before running.
            open('images/' + account + '_image' + str(i) + '.jpg', 'wb').write(r.content)
            print(r.headers.get('content-type'))
            i += 1

        time.sleep(60)
# Downloads in current directory
