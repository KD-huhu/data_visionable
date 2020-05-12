import pandas as pd
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

# get rating、runtime value
runtime_data = df['Runtime (Minutes)'].values
# get max and min
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
# print(max_runtime,min_runtime)
# set group spacing
d = 5
# calculate number of groups
bin_nums = (max_runtime - min_runtime) // d
# print(num_bin)
# draw hist
plt.hist(runtime_data,range(min_runtime.min(), max_runtime.max()+d, d))

# Adjust X-axis scale
plt.xticks(range(min_runtime.min(), max_runtime.max()+d, d))

# Set axis legend
plt.ylabel("电影时间",fontproperties=my_font)
plt.xlabel("电影时长",fontproperties=my_font)
plt.title('电影时间统计',fontproperties=my_font)

# draw grid
plt.grid(alpha=0.3)

#show
plt.show()