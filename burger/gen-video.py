from moviepy.editor import *

clip1 = VideoFileClip("clips/clip1.mp4")
clip2 = VideoFileClip("clips/clip2.mp4")
prices1 = ImageClip("out/burger1.png")

result = concatenate_videoclips([clip1, prices1.set_duration(30), clip2])
result.write_videofile("out/clip.mp4")
