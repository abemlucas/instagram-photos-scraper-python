import requests


url = ''
r = requests.get(url, allow_redirects=True)

open('medicalskinaesthetics_image1.jpg', 'wb').write(r.content)
print(r.headers.get('content-type'))
# Downloads in current directory
