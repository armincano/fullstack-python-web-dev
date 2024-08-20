from product import Product

zara_for_him_100ml= Product("for him",25990,12)
zara_for_him_black_edition_100ml= Product("for him black edition",25990,7)
zara_for_him_red_edition_100ml= Product("for him red edition",25990,1)
db={}
db.update({zara_for_him_100ml.name:zara_for_him_100ml})
db.update({zara_for_him_black_edition_100ml.name:zara_for_him_black_edition_100ml})
db.update({zara_for_him_red_edition_100ml.name:zara_for_him_red_edition_100ml})