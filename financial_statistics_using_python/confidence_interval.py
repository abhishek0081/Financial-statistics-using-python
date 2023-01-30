
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.stats.api as sms
aap1 =pd.read_csv('microsoft.csv',index_col=0);
aap1['logreturn'] =np.log(aap1['Close'].shift(-1))-np.log(aap1['Close']);
z_left = stats.norm.ppf(0.05);
z_right = stats.norm.ppf(0.95);
sample_mean = aap1['logreturn'].mean();
sample_std = aap1['logreturn'].std(ddof=1)/(aap1.shape[0])**0.5;
interval_left = sample_mean-1.64*sample_std;
interval_right = sample_mean+1.64*sample_std;
print("sample mean is",sample_mean);
print(156*"*");
print("90% confidence interval is : ",end ="");

print(interval_left,interval_right);
# stats.norm.interval(alpha=0.9,len(aap1)-1, loc=np.mean(aap1), scale=stats.sem(aap1));
# print(sms.DescrStatsW(aap1).tconfint_mean());