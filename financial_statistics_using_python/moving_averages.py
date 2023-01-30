import pandas as pd
import matplotlib.pyplot as plt

fb =pd.read_csv("facebook.csv",index_col=0);
fb['priceDiff'] = fb['Close'].shift(-1) - fb['Close'];
ms = pd.read_csv("microsoft.csv",index_col=0);
ms['priceDiff'] =  ms['Close'].shift(-1) - ms['Close'];
print(ms['priceDiff'].loc['05-01-2015']);
print(fb['priceDiff'].loc['05-01-2015']);

fb['Return'] = fb['priceDiff']/fb['Close'];
ms['Return'] = ms['priceDiff']/ms['Close'];
print(ms['Return'].loc['05-01-2015']);
print(fb['Return'].loc['05-01-2015']);
fb['Direction'] = [1 if fb['priceDiff'].loc[ei]>0 else 0 for ei in fb.index];
ms['Direction'] = [1 if ms['priceDiff'].loc[ei]>0 else 0 for ei in ms.index];
print('Price Direction on {} is {}. Direction is {} '.format('05-01-2015',ms['priceDiff'].loc['05-01-2015'],ms['Direction'].loc['05-01-2015']));
print(f"Price Direction on {'05-01-2015'} is {ms['priceDiff'].loc['05-01-2015']}.Direction  is {ms['Direction'].loc['05-01-2015']}");
