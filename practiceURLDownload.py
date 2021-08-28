import requests


url = 'https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/171792465_176725177608092_1384533130485842452_n.jpg?_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=108&_nc_ohc=Bg-XPzA7BlkAX-jhMsZ&edm=APU89FABAAAA&ccb=7-4&oh=649b6ed1b2ffa1d2a83089700649737a&oe=612F96DC&_nc_sid=86f79a'
r = requests.get(url, allow_redirects=True)

open('studioabasiskincare_image1.jpg', 'wb').write(r.content)
print(r.headers.get('content-type'))
# Downloads in current directory
