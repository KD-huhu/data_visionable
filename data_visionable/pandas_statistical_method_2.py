import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

# set figure size
plt.figure(figsize=(20,8),dpi=80)

# read cvs file
file_path = './IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

# data screening
# print(df.head(1))
# print(df.info())

# get genre
# print(df['Genre'].head(3))
# Split string
temp_list = df['Genre'].str.split(',').tolist()
# print(temp_list)
# [['Action,Adventure,Sci-Fi'], ['Adventure,Mystery,Sci-Fi'],...]
# temp_list is an iterative object
genre_list = list(set([i for j in temp_list for i in j]))
# print(genre_list)

# Construct all zero array
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)

# Count the number of times
for i in range(df.shape[0]):
    zeros_df.loc[i,temp_list[i]] = 1

# sum
genre_count = zeros_df.sum(axis=0)
# print(genre_count)
# sort
genre_count = genre_count.sort_values()
# print(genre_count)

# draw
_x = genre_count.index
_y = genre_count.values

plt.bar(range(len(_x)),_y,width=0.6)
plt.xticks(list(range(len(_x))),_x,rotation=45)
plt.show()