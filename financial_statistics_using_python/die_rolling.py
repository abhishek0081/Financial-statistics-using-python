from os import replace
from matplotlib import colors
from numpy.core.fromnumeric import sort, var
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core import series
trail =500;
die = pd.DataFrame(list(range(1,7)));
result = [die.sample(2,replace = True).sum().loc[0] for i in range(trail)];
print(f"10 random samples of sum of independent throw of two dies =  {result[:10]}");
freq = pd.DataFrame(result)[0].value_counts();
sort_freq = freq.sort_index();
print(sort_freq);
relative_freq = sort_freq/sort_freq.sum();
relative_freq.plot(kind ="bar",color = "black");


# plt.show();

X_distri = pd.DataFrame(index= list(range(2,13)));
X_distri['prob'] = [1,2,3,4,5,6,5,4,3,2,1];
X_distri['prob'] = X_distri["prob"]/36;
Mean  = pd.Series(X_distri.index*X_distri['prob']).sum();
Variance = pd.Series(((X_distri.index -Mean)**2)*X_distri['prob']).sum();
print(Mean,Variance,X_distri);
result = pd.Series(result);
print(result.mean(),result.var());