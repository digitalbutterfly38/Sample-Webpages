from moviepy.editor import *

# load clips
clip_001 = VideoFileClip ("E:\\100 Days of Code The Complete Python Pro Bootcamp for 2022 Custom\\001 What you're going to get from this course.mp4")
clip_002 = VideoFileClip ("E:\\100 Days of Code The Complete Python Pro Bootcamp for 2022 Custom\\002 START HERE.mp4")
clip_003 = VideoFileClip ("E:\\100 Days of Code The Complete Python Pro Bootcamp for 2022 Custom\\003 Downloadable Resources and Tips for Taking the Course.mp4")

# join + write
result_clip = concatenate_videoclips([clip_001,clip_002,clip_003])
result_clip.write_videofile("E:\\combined_updated.mp4")