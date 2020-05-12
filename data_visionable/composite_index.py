import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

# set figure size
plt.figure(figsize=(20,8),dpi=80)

file_path = './starbucks_store_worldwide.csv'
# read cvs file
df = pd.read_csv(file_path)

# Show top 10 countries in total stores
# get value
data = df.groupby(by='Country').count()['Brand'].sort_values(ascending=False)[:10]

_x = data.index
_y = data.values
x = list(range(len(_x)))

# draw
plt.bar(x,_y,width=0.3)
# width : set bar width

# Adjust X-axis scale
plt.xticks(x,_x)

# Set axis legend
plt.xlabel("国家简写",fontproperties=my_font)
plt.ylabel("店铺数量",fontproperties=my_font)
plt.title('全球星巴克店铺数量前十',fontproperties=my_font)

#show
plt.show()