from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

# set value for axis y
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
# set bar_width
bar_width = 0.2
# set value for axis x
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+2*bar_width for i in x_14]

# set figure size
plt.figure(figsize=(20,8),dpi=80)

# draw
plt.bar(x_14,b_14,width=bar_width,label="9月14日")
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

# Adjust X-axis scale
plt.xticks(x_15,a,fontproperties=my_font)

# draw grid
plt.grid(alpha=0.3)

# set legend
plt.legend(prop=my_font)

# Set axis legend
plt.xlabel("电影名",fontproperties=my_font)
plt.ylabel("票房",fontproperties=my_font)
plt.title('电影票房',fontproperties=my_font)

#show
plt.show()