import sqlite3

products = [  "Fresh Soy Face Cleanser",  "Laneige Water Sleeping Mask",  "Tatcha The Dewy Skin Cream",  "Drunk Elephant C-Firma Vitamin C Day Serum",  "Fenty Beauty Gloss Bomb Universal Lip Luminizer",  "Nars Radiant Creamy Concealer",  "Anastasia Beverly Hills Dipbrow Pomade",  "Sunday Riley Good Genes All-in-One Lactic Acid Treatment",  "Pat McGrath Labs MatteTrance Lipstick",  "Huda Beauty Obsessions Eyeshadow Palette"]

products = sorted(products)

connection = sqlite3.connect("product_list.db")
cursor = connection.cursor()

cursor.execute("create table products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(products)):
  cursor.execute("insert into products (name) values (?)",[products[i]])
  print("added ", products[i])

connection.commit()
connection.close()