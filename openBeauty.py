from context import Instagram
from time import sleep
import pandas

instagram = Instagram()

medias = instagram.get_medias('aryaderm')
variable = pandas.read_csv('instagram.csv')

media = medias[0]
media1 = medias[1]
media2 = medias[2]
media3 = medias[3]
media4 = medias[4]
print(variable, media, media1, media2, media3, media4)
