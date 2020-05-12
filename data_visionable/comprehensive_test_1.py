import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

# set figure size
plt.figure(figsize=(20,8),dpi=80)
# read cvs file
file_path = "./books.csv"
df = pd.read_csv(file_path)

# data screening
# print(df.head(1))
# print(df.info())

# get off the nan in original_publication_year
data1 = df[pd.notnull(df["original_publication_year"])]
# grouped
grouped = data1['average_rating'].groupby(by=data1["original_publication_year"]).mean()
# print(grouped)

_x = grouped.index
_y = grouped.values
x = list(range(len(_x)))

# draw
plt.plot(x,_y)
# Adjust X-axis scale
plt.xticks(x[::10],_x[::10],fontproperties=my_font,rotation=45)

# Set axis legend
plt.xlabel("年份",fontproperties=my_font)
plt.ylabel("评分",fontproperties=my_font)
plt.title('历年图书评分',fontproperties=my_font)

#show
plt.show()