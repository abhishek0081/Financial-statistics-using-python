import numpy as np
import matplotlib.pyplot as plt
# x = np.array([2,3,4,5,6,9]);
# y = np.array([45,41,42,46,47,42]);
# my_range = np.arange(6);

# mean_x = np.mean(x);
# mean_y = np.mean(y);
# var_x  = np.var(x);
# var_y  = np.var(y);
# fig,axis =plt.subplots(1,2,sharey = True);
# axis[0].stem(my_range,x,label = "x values", bottom = mean_x);
# axis[1].stem(my_range,y,label = "y values", bottom = mean_y);
# legend_x = axis[0].legend(loc = "upper right");
# legend_y = axis[1].legend(loc = "lower right");
# plt.show();
# fig,axis =plt.subplots(1,2,sharey = True);
# axis[0].stem(my_range,(x**2 - x),label = "x values", bottom = var_x);
# axis[1].stem(my_range,(y**2 - y),label = "y values", bottom = var_y);
# legend_x = axis[0].legend(loc = "upper right");
# legend_y = axis[1].legend(loc = "lower right");
# plt.show();


data = [[1,2], [3,4], [5,6]]
data = np.array(data)
print(data[:,-1])
print(data.mean(1))
print(np.min(data, 1))
plt.subplots()
