from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

# set value for axis y
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_12 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
# set value for axis x
x_3 = list(range(1,32))
x_12 = list(range(51,82))

# set figure size
plt.figure(figsize=(20,8),dpi=80)

# draw
plt.scatter(x_3,y_3,label='三月')
plt.scatter(x_12,y_12,label='十二月')
# add legend
plt.legend(prop=my_font)

# Adjust X-axis scale
_x = x_3 + x_12
_xticks_labels = ['三月{}日'.format(i) for i in x_3]
_xticks_labels += ['十二月{}日'.format(i) for i in x_3]
plt.xticks(_x[::3],_xticks_labels[::3],fontproperties=my_font)

# Set axis legend
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title('三月份和十二月份气温对比',fontproperties=my_font)

#show
plt.show()