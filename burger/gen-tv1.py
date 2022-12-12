import pandas as pd
from moviepy.editor import *

excel = pd.ExcelFile('../data.xlsx')
data_burger = pd.read_excel(excel, 'Burger').to_dict()
cross_img = ImageClip("../x.png")

# Clip 1
# ------
price1_bf = data_burger['Precios'][28]
price1_aft = data_burger['Precios'][29]
coords1_bf = (int(data_burger['X'][28]), int(data_burger['Y'][28]))
coords1_aft = (int(data_burger['X'][29]), int(data_burger['Y'][29]))

clip1 = VideoFileClip("../clips/tv1-burger1.mp4")
txt1_bf = TextClip(f"${price1_bf}", font="../big_noodle_titling.ttf", color='white', fontsize=140).set_position(coords1_bf).set_duration(15).fadein(2).fadeout(2)
txt1_aft = TextClip(f"${price1_aft}", font="../big_noodle_titling.ttf", color='white', fontsize=220).set_position(coords1_aft).set_duration(15).fadein(2).fadeout(2)
composite1 = CompositeVideoClip([
    clip1, txt1_bf, cross_img.set_position((coords1_bf[0] - 100, coords1_bf[1] - 10)).set_duration(15).resize(5).fadein(2).fadeout(2), txt1_aft
])
# ------

# Clip 2
# ------
price2_bf = data_burger['Precios'][30]
price2_aft = data_burger['Precios'][31]
coords2_bf = (int(data_burger['X'][30]), int(data_burger['Y'][30]))
coords2_aft = (int(data_burger['X'][31]), int(data_burger['Y'][31]))

clip2 = VideoFileClip("../clips/tv1-burger2.mp4")
txt2_bf = TextClip(f"${price2_bf}", font="../big_noodle_titling.ttf", color='white', fontsize=140).set_position(coords2_bf).set_duration(15).fadein(2).fadeout(2)
txt2_aft = TextClip(f"${price2_aft}", font="../big_noodle_titling.ttf", color='white', fontsize=220).set_position(coords2_aft).set_duration(15).fadein(2).fadeout(2)
composite2 = CompositeVideoClip([
    clip2, txt2_bf, cross_img.set_position((coords2_bf[0] - 100, coords2_bf[1] - 30)).set_duration(15).resize(5).fadein(2).fadeout(2), txt2_aft
])
# ------

# Clip 3
# ------
price3 = data_burger['Precios'][32]
coords3 = (int(data_burger['X'][32]), int(data_burger['Y'][32]))

clip3 = VideoFileClip("../clips/tv1-burger3.mp4")
txt3 = TextClip(f"${price3}", font="../big_noodle_titling.ttf", color='white', fontsize=200).set_position(coords3).set_duration(12).fadein(2.2).fadeout(1)
composite3 = CompositeVideoClip([
    clip3, txt3
])
# ------

# Clip 4
# ------
price4 = data_burger['Precios'][33]
coords4 = (int(data_burger['X'][33]), int(data_burger['Y'][33]))

clip4 = VideoFileClip("../clips/tv1-burger4.mp4")
txt4 = TextClip(f"${price4}", font="../big_noodle_titling.ttf", color='white', fontsize=200).set_position(coords4).set_duration(12).fadein(2).fadeout(2)
composite4 = CompositeVideoClip([
    clip4, txt4
])
# ------

result = concatenate_videoclips([composite1, composite2, composite3, composite4]*16) # Generates ~15 minutes
result.write_videofile('../out/tv1-burgerout.mp4', fps=30)
