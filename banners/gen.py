import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

cross_img = Image.open("x.png")

def banner1(d):
    img = Image.open("templates/template-banner1.png")
    draw = ImageDraw.Draw(img)
    font_sml = ImageFont.truetype("big_noodle_titling.ttf", 77)
    font_big = ImageFont.truetype("big_noodle_titling.ttf", 122)

    price_bf = f"${d['Precios'][0]}"
    price_aft = f"${d['Precios'][1]}"
    coords_bf = (d['X'][0], d['Y'][0])
    coords_aft = (d['X'][1], d['Y'][1])

    draw.text(coords_bf, price_bf, WHITE, font=font_sml)
    draw.bitmap((coords_bf[0] - 50, coords_bf[1] - 25), cross_img.resize((260, 140)), RED)
    draw.text(coords_aft, price_aft, WHITE, font=font_big)

    img.save('out/banner1.png')

def banner2(d):
    img = Image.open("templates/template-banner2.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 63)

    price = f"${d['Precios'][2]}"
    coords = (d['X'][2], d['Y'][2])

    draw.text(coords, price, WHITE, font=font)

    img.save('out/banner2.png')

def banner3(d):
    img = Image.open("templates/template-banner3.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 95)

    price = f"${d['Precios'][3]}"
    coords = (d['X'][3], d['Y'][3])

    draw.text(coords, price, WHITE, font=font)

    img.save('out/banner3.png')

def banner4(d):
    img = Image.open("templates/template-banner4.png")
    draw = ImageDraw.Draw(img)
    font_sml = ImageFont.truetype("big_noodle_titling.ttf", 106)
    font_big = ImageFont.truetype("big_noodle_titling.ttf", 150)

    price_bf = f"${d['Precios'][4]}"
    price_aft = f"${d['Precios'][5]}"
    coords_bf = (d['X'][4], d['Y'][4])
    coords_aft = (d['X'][5], d['Y'][5])

    draw.text((coords_bf[0] + 5, coords_bf[1] + 5), price_bf, BLACK, font=font_sml)
    draw.text(coords_bf, price_bf, WHITE, font=font_sml)
    draw.bitmap((0, coords_bf[1] - 15), cross_img.resize((320, 140)), RED) # why the fuck 0?
    draw.text((coords_aft[0] + 5, coords_aft[1] + 5), price_aft, BLACK, font=font_big)
    draw.text(coords_aft, price_aft, WHITE, font=font_big)

    img.save('out/banner4.png')

def banner5(d):
    img = Image.open("templates/template-banner5.png")
    draw = ImageDraw.Draw(img)
    font_sml = ImageFont.truetype("big_noodle_titling.ttf", 78)
    font_big = ImageFont.truetype("big_noodle_titling.ttf", 130)

    price_bf = f"${d['Precios'][6]}"
    price_aft = f"${d['Precios'][7]}"
    coords_bf = (d['X'][6], d['Y'][6])
    coords_aft = (d['X'][7], d['Y'][7])

    # Optional: shadowed text
    #draw.text((coords_bf[0] + 5, coords_bf[1] + 5), price_bf, BLACK, font=font_sml)
    draw.text(coords_bf, price_bf, WHITE, font=font_sml)
    draw.bitmap((coords_bf[0] + 10, coords_bf[1] - 60), cross_img.resize((120, 220)), RED)
    #draw.text((coords_aft[0] + 5, coords_aft[1] + 5), price_aft, BLACK, font=font_big)
    draw.text(coords_aft, price_aft, WHITE, font=font_big)

    img.save('out/banner5.png')

def banner6(d):
    img = Image.open("templates/template-banner6.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("big_noodle_titling.ttf", 115)

    price = f"${d['Precios'][8]}"
    coords = (d['X'][8], d['Y'][8])

    draw.text(coords, price, WHITE, font=font)

    img.save('out/banner6.png')

