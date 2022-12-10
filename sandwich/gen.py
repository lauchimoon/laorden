import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from moviepy.editor import *

WHITE = (255, 255, 255)

# Generate price tables for first template
def sandwich1(d):
    img = Image.open("./templates/template-sandwich1.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 60)

    for i in range(0, 20):
        product = d['Productos'][i]
        price   = f"{d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    img.save('./out/sandwich1.png')

# Generate price tables for second template
def sandwich2(d):
    img = Image.open("./templates/template-sandwich2.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 120)

    for i in range(20, 25):
        product = d['Productos'][i]
        price   = f"{d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    img.save('./out/sandwich2.png')

# Generate price tables for third template
def sandwich3(d):
    img = Image.open("./templates/template-sandwich3.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 120)

    for i in range(25, 31):
        product = d['Productos'][i]
        price   = f"{d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    img.save('./out/sandwich3.png')

# Generate price tables for fourth template
def sandwich4(d):
    COLOR = (72, 112, 41)

    img = Image.open("./templates/template-sandwich4.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 200)

    idx = 30
    product = d['Productos'][idx]
    price   = f"${d['Precios'][idx]}"
    x       = 15.0
    y       = 0.0
    coords  = (int(x), int(y))
    draw.text(coords, price, COLOR, font=font)

    img.save('./out/sandwich4.png')

# Generate video. Requires generated images
def video():
    DUR_1 = 10
    DUR_2 = 15
    FADE = 1
    REPEAT = 10

    clips = [ # Lasts 1:40 with 60 fps.
        ImageClip("clips/1.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip("out/sandwich1.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
        ImageClip("clips/3.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip("out/sandwich2.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
        ImageClip("clips/5.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip("out/sandwich3.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
        ImageClip("clips/7.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip("out/sandwich4.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
    ]

    result = concatenate_videoclips(clips*REPEAT)
    result.write_videofile('out/clip.mp4', fps=30)

data = pd.read_excel('./data.xlsx').to_dict()

if not os.path.exists('out/'): # Does output dir exist?
    os.mkdir('out/')

print("Generating promotional images")
sandwich1(data)
print("Generated out/sandwich1.png. Next")
sandwich2(data)
print("Generated out/sandwich2.png. Next")
sandwich3(data)
print("Generated out/sandwich3.png. Next")
sandwich4(data)
print("Generated out/sandwich4.png. Next")
video()
print("Finish")
