import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from moviepy.editor import *
import datetime

WHITE = (255, 255, 255)
today = datetime.date.today().strftime('%d-%m-%Y')

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

    filename = f"./resources/Cartel-Burger-1-{today}.png"
    img.save(filename)

def tv1(d):
    cross_img = ImageClip("./x.png")

    # Clip 1
    # ------
    price1_bf = d['Precios'][28]
    price1_aft = d['Precios'][29]
    coords1_bf = (int(d['X'][28]), int(d['Y'][28]))
    coords1_aft = (int(d['X'][29]), int(d['Y'][29]))

    clip1 = VideoFileClip("./clips/tv1-burger1.mp4")
    txt1_bf = TextClip(f"${price1_bf}", font="./big_noodle_titling.ttf", color='white', fontsize=140).set_position(coords1_bf).set_duration(15).fadein(2).fadeout(2)
    txt1_aft = TextClip(f"${price1_aft}", font="./big_noodle_titling.ttf", color='white', fontsize=220).set_position(coords1_aft).set_duration(15).fadein(2).fadeout(2)
    composite1 = CompositeVideoClip([
        clip1, txt1_bf, cross_img.set_position((coords1_bf[0] - 100, coords1_bf[1] - 10)).set_duration(15).resize(5).fadein(2).fadeout(2), txt1_aft
    ])
    # ------

    # Clip 2
    # ------
    price2_bf = d['Precios'][30]
    price2_aft = d['Precios'][31]
    coords2_bf = (int(d['X'][30]), int(d['Y'][30]))
    coords2_aft = (int(d['X'][31]), int(d['Y'][31]))

    clip2 = VideoFileClip("./clips/tv1-burger2.mp4").set_duration(5)
    txt2_bf = TextClip(f"${price2_bf}", font="./big_noodle_titling.ttf", color='white', fontsize=140).set_position(coords2_bf).set_duration(15).fadein(2).fadeout(2)
    txt2_aft = TextClip(f"${price2_aft}", font="./big_noodle_titling.ttf", color='white', fontsize=220).set_position(coords2_aft).set_duration(15).fadein(2).fadeout(2)
    composite2 = CompositeVideoClip([
        clip2, txt2_bf, cross_img.set_position((coords2_bf[0] - 100, coords2_bf[1] - 30)).set_duration(15).resize(5).fadein(2).fadeout(2), txt2_aft
    ])
    # ------

    # Clip 3
    # ------
    price3 = d['Precios'][32]
    coords3 = (int(d['X'][32]), int(d['Y'][32]))

    clip3 = VideoFileClip("./clips/tv1-burger3.mp4")
    txt3 = TextClip(f"${price3}", font="./big_noodle_titling.ttf", color='white', fontsize=200).set_position(coords3).set_duration(12).fadein(2.2).fadeout(1)
    composite3 = CompositeVideoClip([
        clip3, txt3
    ])
    # ------

    # Clip 4
    # ------
    price4 = d['Precios'][33]
    coords4 = (int(d['X'][33]), int(d['Y'][33]))

    clip4 = VideoFileClip("./clips/tv1-burger4.mp4")
    txt4 = TextClip(f"${price4}", font="./big_noodle_titling.ttf", color='white', fontsize=200).set_position(coords4).set_duration(12).fadein(2).fadeout(2)
    composite4 = CompositeVideoClip([
        clip4, txt4
    ])
    # ------

    result = concatenate_videoclips([composite1, composite2, composite3, composite4]*16) # Generates ~15 minutes
    filename = f"./out/Video-Burger-1-{today}.mp4"
    result.write_videofile(filename, fps=30)

def tv2():
    filename1 = f"./resources/Cartel-Burger-1-{today}.png"
    table = ImageClip(filename1).set_duration(25).fadein(1).fadeout(1)
    clip1 = VideoFileClip('./clips/tv2-burger1.mp4')
    clip2 = VideoFileClip('./clips/tv2-burger2.mp4')
    clip3 = VideoFileClip('./clips/tv2-burger3.mp4')
    clip4 = VideoFileClip('./clips/tv2-burger4.mp4')
    clip5 = VideoFileClip('./clips/tv2-burger5.mp4')
    clip6 = VideoFileClip('./clips/tv2-burger6.mp4')
    clip7 = VideoFileClip('./clips/tv2-burger7.mp4')
    clip8 = VideoFileClip('./clips/tv2-burger8.mp4')
    clip9 = VideoFileClip('./clips/tv2-burger9.mp4')

    result = concatenate_videoclips([
        clip1, table, clip2, table, clip3, table, clip4, table,
        clip5, table, clip6, table, clip7, table, clip8, table,
        clip9, table
    ]*4)

    filename2 = f"./out/Video-Burger-2-{today}.mp4"
    result.write_videofile(filename2, fps=30)

def tv3(d):
    # Image part
    # ----------
    img = Image.open('./templates/template-burger3.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./big_noodle_titling.ttf', 85)

    for i in range(34, 50):
        price = f"${d['Precios'][i]}"
        x = d['X'][i]
        y = d['Y'][i]
        coords = (int(x), int(y))

        draw.text(coords, price, WHITE, font=font)

    filename1 = f"./resources/Cartel-Burger-3-{today}.png"
    img.save(filename1)
    # ----------

    # Video part
    # ----------
    clip1 = VideoFileClip('./clips/tv3-burger1.mp4')
    clip2 = VideoFileClip('./clips/tv3-burger2.mp4').fadein(1).fadeout(1)
    clip3 = VideoFileClip('./clips/tv3-burger3.mp4').fadein(1).fadeout(1)
    clip4 = VideoFileClip('./clips/tv3-burger4.mp4')
    table = ImageClip(filename1).set_duration(30).fadein(2).fadeout(2)

    result = concatenate_videoclips([
        clip1, table, clip2, table, clip3, table, clip4, table
    ]*6) # Generates ~16 minutes

    filename2 = f"./out/Video-Burger-3-{today}.mp4"
    result.write_videofile('./out/tv3-burgerout.mp4', fps=30)
    # ----------

