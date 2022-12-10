import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from moviepy.editor import *

WHITE = (255, 255, 255)

# Generate price tables for first template
def burger1(d):
    img = Image.open("templates/template-burger1.png")
    draw = ImageDraw.Draw(img)
    font_big = ImageFont.truetype("big_noodle_titling.ttf", 57)
    font_sml = ImageFont.truetype("big_noodle_titling.ttf", 42)

    for i in range(0, 22): # Burgers
        price   = f"${d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font_big)

    for i in range(22, 25): # Drinks
        price   = f"${d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font_sml)

    img.save('./out/burger1.png')

# Generate price tables for second template
def burger2(d):
    img = Image.open("templates/template-burger2.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 80)

    for i in range(25, 32):
        price   = f"${d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    img.save('./out/burger2.png')

# Generate video. Requires generated images
def burger_video():
    clip1 = VideoFileClip("clips/clip1.mp4")
    clip2 = VideoFileClip("clips/clip2.mp4")
    prices1 = ImageClip("out/burger1.png")

    result = concatenate_videoclips([clip1, prices1.set_duration(30), clip2])
    result.write_videofile("out/clip.mp4")

