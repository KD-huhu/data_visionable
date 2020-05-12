from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

# set value for axis y
y_my = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_dm = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
# set value for axis x
x = list(range(11,31))

# set figure size
plt.figure(figsize=(20,8),dpi=80)
# draw
plt.plot(x,y_my,label='自己')
plt.plot(x,y_dm,label='同桌')

# Adjust X-axis scale
_xticks_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x,_xticks_labels,fontproperties=my_font)

# add grid
plt.grid(alpha=0.1)

# add legend
plt.legend(prop=my_font)

#show
plt.show()