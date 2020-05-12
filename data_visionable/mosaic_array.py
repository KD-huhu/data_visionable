import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# set figure size
plt.figure(figsize=(20,8),dpi=80)
# read file
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

us_data = np.loadtxt(us_file_path,delimiter=",",dtype="int")
uk_data = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

# all 0 -- us
zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
# all 1 -- uk
ones_data = np.ones((uk_data.shape[0],1)).astype(int)

# add country info
us_data = np.hstack((us_data,zeros_data))
uk_data = np.hstack((uk_data,ones_data))

# mosaic array
final_data = np.vstack((us_data,uk_data))

# print(final_data)
