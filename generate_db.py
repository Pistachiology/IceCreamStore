from store.models import *

flavour = [
    'Chocolate Chip',
    'Cookie Dough',
    'Rainbow Sherbet',
    'Vanilla',
    'Chocolate Mint',
    'Jamoca',
    'Rocky Road',
    'Very Berry Strawberry',
    'Chocolate',
    'Paline and Cream'
]

icecream_img = [
    'choc-chip.jpg',
    'cookie-dough.jpg', 
    'RainbowSherbet.jpg',
    'vanilla.jpg',
    'choc-mint.png',
    'jamoca.png',
    'RockyRoad2.jpg',
    'very-berry-stawberry.png',
    'chocolate.png',
    'paline-n-cream.png',
    'showflavour.jpg'     
]

for i in range(10):
    prod = Product.objects.get(id=i+1) 
    prod.name = flavour[i]
    # prod.description = desciption[i]
    prod.image = '/static/product_image/' + icecream_img[i]
    prod.save()
