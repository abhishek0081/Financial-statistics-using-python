import pandas as pd
import matplotlib.pyplot as plt

fb = pd.read_csv("facebook.csv");
fb['MA10'] = fb['Close'].rolling(10).mean();
fb['MA50'] = fb['Close'].rolling(50).mean();
fb =fb.dropna();
fb.head();
fb['Shares'] = [1 if fb.loc[ei ,'MA10']>fb.loc[ei,"MA50"] else 0 for ei in fb.index];
fb['Close1'] = fb['Close'].shift(-1);
fb['Profit'] = [fb.loc[ei,"Close1"] - fb.loc[ei,"Close"] if fb.loc[ei,"Shares"] == 1 else 0 for ei in fb.index];
fb["Profit"].plot();
plt.axhline(y=0,color = "red");
plt.show();
fb["Wealth"] = fb["Profit"].cumsum();
fb.tail();

fb["Wealth"].plot();
plt.title(f"Total money you win is{fb.loc[fb.index[-2],'Wealth']}");
plt.show();

###############   Microsoft   #####################
import pandas as pd
import matplotlib.pyplot as plt

ms = pd.read_csv("microsoft.csv");
ms['MA10'] = ms['Close'].rolling(10).mean();
ms['MA50'] = ms['Close'].rolling(50).mean();
ms =ms.dropna();
ms.head();
ms['Shares'] = [1 if ms.loc[ei ,'MA10']>ms.loc[ei,"MA50"] else 0 for ei in ms.index];
ms['Close1'] = ms['Close'].shift(-1);
ms['Profit'] = [ms.loc[ei,"Close1"] -ms.loc[ei,"Close"] if ms.loc[ei,"Shares"] == 1 else 0 for ei in ms.index];
ms["Profit"].plot();
plt.axhline(y=0,color = "red");
plt.show();
ms["Wealth"] = ms["Profit"].cumsum();
ms.tail();

ms["Wealth"].plot();
plt.title(f"Total money you win is{ms.loc[ms.index[-2],'Wealth']}");
plt.show();

##################  TSLA  ##################
tsla = pd.read_csv("TSLA.csv");
tsla['MA10'] = tsla['Close'].rolling(10).mean();
tsla['MA50'] = tsla['Close'].rolling(50).mean();
tsla =tsla.dropna();
tsla.head();
tsla['Shares'] = [1 if tsla.loc[ei ,'MA10']>tsla.loc[ei,"MA50"] else 0 for ei in tsla.index];
tsla['Close1'] = tsla['Close'].shift(-1);
tsla['Profit'] = [tsla.loc[ei,"Close1"] -tsla.loc[ei,"Close"] if tsla.loc[ei,"Shares"] == 1 else 0 for ei in tsla.index];
tsla["Profit"].plot();
plt.axhline(y=0,color = "blue");
plt.show();
tsla["Wealth"] = tsla["Profit"].cumsum();
tsla.tail();

plt.title(f"Total money you win is{tsla.loc[tsla.index[-2],'Wealth']}");
tsla["Wealth"].plot();
plt.show();