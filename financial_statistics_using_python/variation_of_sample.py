
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from pandas.io.parsers import read_csv
# from pandas.core.frame import DataFrame
from scipy import stats

Fstsample = pd.DataFrame(np.random.normal(0,1,size =1000));
print('Sample mean is',Fstsample[0].mean());
print('sample SD is ',Fstsample[0].std(ddof=1));
meanlist = [];
varlist = [];
for t in range(1000):
    sample = pd.DataFrame(np.random.normal(0,1,size=30));
    meanlist.append(sample[0].mean());
    varlist.append(sample[0].var(ddof=1));


collection = pd.DataFrame();
collection['meanlist'] =meanlist;
collection['varlist'] = varlist;
collection['meanlist'].hist(bins = 500);

# collection['meanlist'].hist(bins=500);
# plt.plot(collection['meanlist'],stats.norm.pdf(collection['meanlist'],0,1));
plt.show();
collection['varlist'].hist(bins = 500);
plt.show();
samplemeanlist = [];
apop =  pd.DataFrame([1,0,0,0,1,0,0,0,1]);
for t in range(100000):
    sample = apop[0].sample(2000,replace =True);
    samplemeanlist.append(sample.mean());

acollec =pd.DataFrame();
acollec['meanlist'] = samplemeanlist;
acollec['meanlist'].hist(bins=250,color='magenta');
plt.show();
