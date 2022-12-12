import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from moviepy.editor import *
import datetime

WHITE = (255, 255, 255)
today = datetime.date.today().strftime('%d-%m-%Y')

# Generate price tables for first template
def sandwich1(d):
    img = Image.open("templates/template-sandwich1.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 60)

    for i in range(0, 20):
        price   = f"{d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    filename = f"resources/sandwich1-{today}.png"
    img = img.transpose(Image.ROTATE_270)
    img.save(filename)

# Generate price tables for second template
def sandwich2(d):
    img = Image.open("templates/template-sandwich2.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 120)

    for i in range(20, 25):
        price   = f"{d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    filename = f"resources/sandwich2-{today}.png"
    img = img.transpose(Image.ROTATE_270)
    img.save(filename)

# Generate price tables for third template
def sandwich3(d):
    img = Image.open("templates/template-sandwich3.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 120)

    for i in range(25, 31):
        price   = f"{d['Precios'][i]}"
        x       = d['X'][i]
        y       = d['Y'][i]
        coords  = (int(x), int(y))
        draw.text(coords, price, WHITE, font=font)

    filename = f"resources/sandwich3-{today}.png"
    img = img.transpose(Image.ROTATE_270)
    img.save(filename)

# Generate price tables for fourth template
def sandwich4(d):
    COLOR = (72, 112, 41)

    img = Image.open("templates/template-sandwich4.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 200)

    idx = 30
    price   = f"${d['Precios'][idx]}"
    x       = 15.0
    y       = 0.0
    coords  = (int(x), int(y))
    draw.text(coords, price, COLOR, font=font)

    filename = f"resources/sandwich4-{today}.png"
    img = img.transpose(Image.ROTATE_270)
    img.save(filename)

# Generate video. Requires generated images
def sandwich_video():
    DUR_1 = 10
    DUR_2 = 15
    FADE = 1
    REPEAT = 10

    clips = [ # Lasts 1:40 with 60 fps.
        ImageClip("clips/sandwich1.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip(f"resources/sandwich1-{today}.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
        ImageClip("clips/sandwich3.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip(f"resources/sandwich2-{today}.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
        ImageClip("clips/sandwich5.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip(f"resources/sandwich3-{today}.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
        ImageClip("clips/sandwich7.png").set_duration(DUR_1).fadein(FADE).fadeout(FADE),
        ImageClip(f"resources/sandwich4-{today}.png").set_duration(DUR_2).fadein(FADE).fadeout(FADE),
    ]

    result = concatenate_videoclips(clips*REPEAT)
    filename = f"out/Video-Sandwich-Lagos-{today}.mp4"
    result.write_videofile(filename, fps=30)

