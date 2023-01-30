########### Big drop in apple price #############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from pandas.io.sql import DatabaseError
from scipy.stats import norm
from scipy.stats.morestats import Std_dev

apple = pd.read_csv("apple.csv",index_col= 0);
apple.loc['01-08-2012':'01-08-2013','Close'].plot();
plt.show();

apple['LogReturn'] = np.log(apple['Close']).shift(-1) - np.log(apple['Close']);

density  = pd.DataFrame();
mu = apple['LogReturn'].mean();
sigma = apple['LogReturn'].std(ddof =1);
print(mu,sigma);

density["x"] = np.arange(apple['LogReturn'].min()-0.01,apple['LogReturn'].max()+0.01, 0.001);
density['pdf'] = norm.pdf(density['x'],mu,sigma);
density['cdf'] = norm.cdf(density['x'],0,1);

# plt.show();
# plt.plot(density['x'],density['cdf']);
# plt.show();


# plt.ylim(0,20);
plt.plot(density["x"],density['pdf']);
plt.fill_between(x=np.arange(-0.1,0.05,0.0001),y2 = 0, y1 = norm.pdf(np.arange(-0.1,0.05,0.0001),mu,sigma),facecolor = "pink",alpha =0.5);
apple['LogReturn'].hist(bins=50,figsize=(15, 8));
plt.plot(density['x'],density['pdf']);
plt.show();
prob_return1 = norm.cdf(-0.05,mu,sigma);
print(f"The probability is {prob_return1}");
mu220 = 220*mu;
sigma220 = (220**0.5)*sigma;
print(mu220,sigma220);
print(f"The Probability of dropping over 40 in 220  days is {norm.cdf(-0.4,mu220,sigma220)}");
print(f"The Probability of dropping over 20 in 220  days is {norm.cdf(-0.2,mu220,sigma220)}");

vaR = norm.ppf(0.05,mu,sigma);
print("Single day value at risk",vaR);
# Quatile 
# 5% quantile
print('5% quantile ', norm.ppf(0.05, mu, sigma));
# 95% quantile
print('95% quantile ', norm.ppf(0.95, mu, sigma));
#75%
print('75% quantile ', norm.ppf(0.75, mu, sigma));
#25%
print('25% quantile ', norm.ppf(0.25, mu, sigma));


