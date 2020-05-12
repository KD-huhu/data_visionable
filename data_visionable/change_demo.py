from matplotlib import pyplot as plt

# set axis x
x = range(2,26,2)
# set axis y
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

# set figure size
plt.figure(figsize=(20,8),dpi=80)

# draw
plt.plot(x,y)

# set axis x content
_xtick_label = [i/2 for i in range(4,49)]
# add axis x content
plt.xticks(_xtick_label)
plt.yticks(range(min(y),max(y)+1))

# save
plt.savefig('./first.png')
# show
plt.show()