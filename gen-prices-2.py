# Generate prices table from spreadsheet
# Script valid for templates/template-burger2.png

import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

WHITE = (255, 255, 255)

img = Image.open("./templates/template-burger2.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("big_noodle_titling.ttf", 80)

data = pd.read_excel('./data.xlsx').to_dict()

for i in range(25, 32):
    product = data['Productos'][i]
    price   = f"${data['Precios'][i]}"
    x       = data['X'][i]
    y       = data['Y'][i]
    coords  = (int(x), int(y))
    draw.text(coords, price, WHITE, font=font)

img.save('./out/burger2.png')
