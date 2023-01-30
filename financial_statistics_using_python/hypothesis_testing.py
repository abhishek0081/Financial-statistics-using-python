from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.stats.api as sms
BSE =pd.read_csv(r'D:\OneDrive\Desktop\financial_statistics_using_python\31-03-2020-TO-30-03-2022BSEALLN.csv');
BSE['logreturn'] =np.log(BSE['Close Price'].shift(-1))-np.log(BSE['Close Price']);
plt.title("Close Price of BSE from 2020 to 2022 ",size = 30);
plt.xlabel("Time",size = 20);
plt.ylabel("US $",size = 20);
plt.plot(BSE.loc[:,'Close Price']);
plt.show();
# BSE['logreturn'].plot(figsize=(20,8));
plt.title("Daily Return of BSE from 2020 to 2022",size = 30);
plt.xlabel("Time",size = 20);
plt.ylabel("US $",size = 20);
plt.xlim(BSE.index[0],BSE.index[-1]);

plt.plot(BSE.loc[:,'logreturn']);
plt.axhline(0,color="red");
plt.show();

plt.title("Histogram of Daily Return of BSE from 2020 to 2022",size =30);
BSE.loc[:,'logreturn'].dropna().hist(bins=100);
plt.show();

############### Hypothesis Testing ##################
## Ho : mu = 0
## H1 : mu != 0;
## under Ho
## |x.bar -mu| ------------> Not very large
## standarization
xbar = BSE['logreturn'].mean();
sd = BSE['logreturn'].std(ddof =1);
n = BSE['logreturn'].shape[0];
zhat = (xbar-0)/(sd/(n**0.5));
print(zhat);
alpha = 0.05;  ### 5% los
zleft = stats.norm.ppf(alpha/2,0,1);
zright = -zleft;
print(zleft,zright);
print('At the significance level of ',alpha);
print('shall we reject ? :',zhat>zright or zhat<zleft);


####  Hypothesis for one tail test 
# Null Hypothesis  Ho : ,mu <= 0;
# H1:  mu >0

alpha = 0.05;  ### 5% los
zright = stats.norm.ppf(1-alpha,0,1);
print(zright);
print('At the significance level of ',alpha);
print('shall we reject ? :',zhat>zright);

######## using P value  ##############
##### pvalue < alpha : reject Ho

alpha = 0.05;  ### 5% los
p = stats.norm.cdf(abs(zhat),0,1);
print(p);
print('At the significance level of ',alpha);
print('shall we reject ? :',p<alpha);


