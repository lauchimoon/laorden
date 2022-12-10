import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

cross_img = Image.open("x.png")
data = pd.read_excel("data.xlsx").to_dict()

def banner1():
    img = Image.open("templates/1.png")
    draw = ImageDraw.Draw(img)
    font_sml = ImageFont.truetype("../big_noodle_titling.ttf", 77)
    font_big = ImageFont.truetype("../big_noodle_titling.ttf", 122)

    price_bf = f"${data['Precios'][0]}"
    price_aft = f"${data['Precios'][1]}"
    coords_bf = (data['X'][0], data['Y'][0])
    coords_aft = (data['X'][1], data['Y'][1])

    draw.text(coords_bf, price_bf, WHITE, font=font_sml)
    draw.bitmap((coords_bf[0] - 50, coords_bf[1] - 25), cross_img.resize((260, 140)), RED)
    draw.text(coords_aft, price_aft, WHITE, font=font_big)

    img.save('./out/banner1.png')

def banner2():
    img = Image.open("templates/2.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 63)

    price = f"${data['Precios'][2]}"
    coords = (data['X'][2], data['Y'][2])

    draw.text(coords, price, WHITE, font=font)

    img.save('./out/banner2.png')

def banner3():
    img = Image.open("templates/3.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 95)

    price = f"${data['Precios'][3]}"
    coords = (data['X'][3], data['Y'][3])

    draw.text(coords, price, WHITE, font=font)

    img.save('./out/banner3.png')

def banner4():
    img = Image.open("templates/4.png")
    draw = ImageDraw.Draw(img)
    font_sml = ImageFont.truetype("../big_noodle_titling.ttf", 106)
    font_big = ImageFont.truetype("../big_noodle_titling.ttf", 150)

    price_bf = f"${data['Precios'][4]}"
    price_aft = f"${data['Precios'][5]}"
    coords_bf = (data['X'][4], data['Y'][4])
    coords_aft = (data['X'][5], data['Y'][5])

    draw.text((coords_bf[0] + 5, coords_bf[1] + 5), price_bf, BLACK, font=font_sml)
    draw.text(coords_bf, price_bf, WHITE, font=font_sml)
    draw.bitmap((0, coords_bf[1] - 15), cross_img.resize((320, 140)), RED) # why the fuck 0?
    draw.text((coords_aft[0] + 5, coords_aft[1] + 5), price_aft, BLACK, font=font_big)
    draw.text(coords_aft, price_aft, WHITE, font=font_big)

    img.save('./out/banner4.png')

def banner5():
    img = Image.open("templates/5.png")
    draw = ImageDraw.Draw(img)
    font_sml = ImageFont.truetype("../big_noodle_titling.ttf", 78)
    font_big = ImageFont.truetype("../big_noodle_titling.ttf", 130)

    price_bf = f"${data['Precios'][6]}"
    price_aft = f"${data['Precios'][7]}"
    coords_bf = (data['X'][6], data['Y'][6])
    coords_aft = (data['X'][7], data['Y'][7])

    # Optional: shadowed text
    #draw.text((coords_bf[0] + 5, coords_bf[1] + 5), price_bf, BLACK, font=font_sml)
    draw.text(coords_bf, price_bf, WHITE, font=font_sml)
    draw.bitmap((coords_bf[0] + 10, coords_bf[1] - 60), cross_img.resize((120, 220)), RED)
    #draw.text((coords_aft[0] + 5, coords_aft[1] + 5), price_aft, BLACK, font=font_big)
    draw.text(coords_aft, price_aft, WHITE, font=font_big)

    img.save('./out/banner5.png')

def banner6():
    img = Image.open("templates/6.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../big_noodle_titling.ttf", 115)

    price = f"${data['Precios'][8]}"
    coords = (data['X'][8], data['Y'][8])

    draw.text(coords, price, WHITE, font=font)

    img.save('./out/banner6.png')


if not os.path.exists('out/'): # Does output dir exist?
    os.mkdir('out/')

print("Generating promotional images")
banner1()
print("Generated out/banner1.png. Next")
banner2()
print("Generated out/banner2.png. Next")
banner3()
print("Generated out/banner3.png. Next")
banner4()
print("Generated out/banner4.png. Next")
banner5()
print("Generated out/burger5.png. Next")
banner6()
print("Generated out/burger6.png. Finish")
