from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

# set figure size
plt.figure(figsize=(20,8),dpi=80)

plt.bar(interval,quantity,width=width)

# Adjust X-axis scale
temp_d = [5] + width[:-1]
_x = [i-temp_d[interval.index(i)]*0.5 for i in interval]
plt.xticks(_x,interval)

plt.grid(alpha=0.4)
plt.show()