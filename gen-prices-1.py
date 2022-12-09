# Generate prices table from spreadsheet
# Script valid for burger1.png

import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

WHITE = (255, 255, 255)

img = Image.open("./templates/template-burger1.png")
draw = ImageDraw.Draw(img)
font_big = ImageFont.truetype("big_noodle_titling.ttf", 57)
font_sml = ImageFont.truetype("big_noodle_titling.ttf", 42)

data = pd.read_excel('./data.xlsx').to_dict()

for i in range(0, 22): # Burgers
    product = data['Productos'][i]
    price   = f"${data['Precios'][i]}"
    x       = data['X'][i]
    y       = data['Y'][i]
    coords  = (int(x), int(y))
    draw.text(coords, price, WHITE, font=font_big)

for i in range(22, 25): # Drinks
    product = data['Productos'][i]
    price   = f"${data['Precios'][i]}"
    x       = data['X'][i]
    y       = data['Y'][i]
    coords  = (int(x), int(y))
    draw.text(coords, price, WHITE, font=font_sml)

img.save('./out/burger1.png')
