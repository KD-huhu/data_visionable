import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# set figure size
plt.figure(figsize=(20,8),dpi=80)

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")

# get number of comments
t_us_comments = t_us[:,-1]

# Filter data with more than 5000 comments
t_us_comments = t_us_comments[t_us_comments <= 5000]

# set group spacing
d = 50
bin_nums = (t_us_comments.max()-t_us_comments.min())//d
# print(bin_nums)

# draw hist
plt.hist(t_us_comments,range(t_us_comments.min(), t_us_comments.max()+bin_nums, bin_nums))

# Adjust X-axis scale
plt.xticks(range(t_us_comments.min(), t_us_comments.max()+bin_nums, bin_nums),rotation=45)

# draw grid
plt.grid(alpha=0.3)

#show
plt.show()