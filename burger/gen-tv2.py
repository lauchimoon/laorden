import pandas as pd
from moviepy.editor import *

excel = pd.ExcelFile('../data.xlsx')
data_burger = pd.read_excel(excel, 'Burger').to_dict()

table = ImageClip('../out/burger1.png').set_duration(40).fadein(1).fadeout(1)
clip1 = VideoFileClip('../clips/tv2-burger1.mp4')
clip2 = VideoFileClip('../clips/tv2-burger2.mp4')
clip3 = VideoFileClip('../clips/tv2-burger3.mp4')
clip4 = VideoFileClip('../clips/tv2-burger4.mp4')

result = concatenate_videoclips([
    clip1, table, clip2, table, clip3, table, clip4, table
]*4) # Generates ~17 minutes

result.write_videofile('../out/tv2-burgerout.mp4', fps=30)
