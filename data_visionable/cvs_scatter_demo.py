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
# Filter data with more than 5000 comments
t_us = t_us[t_us[:,1] <= 500000]

# get number of comments
t_us_comments = t_us[:,-1]
# get number of likes
t_us_likes = t_us[:,1]

# draw scatter
plt.scatter(t_us_likes,t_us_comments)

#show
plt.show()