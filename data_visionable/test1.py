from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# Set Chinese font
my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')
# set value for axis x
x = range(0,120)
# set value for axis y
y = [random.randint(20,35) for i in range(120)]

# set figure size
plt.figure(figsize=(20,8),dpi=80)
# draw
plt.plot(x,y)

# Adjust X-axis scale
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]

plt.xticks(list(x)[::3],_xticks_labels[::3],rotation=45,fontproperties=my_font)

# Set legend
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title('10点到12点每分钟的气温变化情况',fontproperties=my_font)

#show
plt.show()