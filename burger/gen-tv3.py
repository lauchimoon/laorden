import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from moviepy.editor import *

# Image part
# ----------
excel = pd.ExcelFile('../data.xlsx')
data_burger = pd.read_excel(excel, 'Burger').to_dict()

img = Image.open('../templates/template-burger3.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('../big_noodle_titling.ttf', 85)

WHITE = (255, 255, 255)

for i in range(34, 50):
    price = f"${data_burger['Precios'][i]}"
    x = data_burger['X'][i]
    y = data_burger['Y'][i]
    coords = (int(x), int(y))

    draw.text(coords, price, WHITE, font=font)

img.save('../out/burger3.png')
# ----------

# Video part
# ----------
clip1 = VideoFileClip('../clips/tv3-burger1.mp4')
clip2 = VideoFileClip('../clips/tv3-burger2.mp4').fadein(1).fadeout(1)
clip3 = VideoFileClip('../clips/tv3-burger3.mp4').fadein(1).fadeout(1)
clip4 = VideoFileClip('../clips/tv3-burger4.mp4')
table = ImageClip('../out/burger3.png').set_duration(30).fadein(2).fadeout(2)

result = concatenate_videoclips([
    clip1, table, clip2, table, clip3, table, clip4, table
]*6)

result.write_videofile('../out/tv3-burgerout.mp4', fps=30)
# ----------
