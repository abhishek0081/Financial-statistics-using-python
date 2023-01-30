import pandas as pd
import matplotlib.pyplot as plt
fb =pd.read_csv("facebook.csv");
ms = pd.read_csv("microsoft.csv");
fb['ma50'] =fb['Close'].rolling(50).mean();
plt.figure(figsize=(10,8));
fb['ma50'].loc['01-01-2015':'31-12-2015'].plot(label = 'Moving AVerage at lag 50');
fb['Close'].loc['01-01-2015':'31-12-2015'].plot(label = 'Close');
plt.legend();
plt.show();
ms['ma60'] =ms['Close'].rolling(60).mean();
plt.figure(figsize=(10,8));
ms['ma60'].loc['01-01-2015':'31-12-2015'].plot(label = 'Moving Average at lag 50');
ms['Close'].loc['01-01-2015':'31-12-2015'].plot(label = 'Close');
plt.legend();
plt.show();