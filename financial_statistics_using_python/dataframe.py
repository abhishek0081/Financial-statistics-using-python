import pandas as pd
import matplotlib.pyplot as plt

fb = pd.read_csv("facebook.csv",index_col = 0);
# print(fb);
# print(fb.shape);
# print(fb.describe());
# print(fb.iloc[-1,0]);
plt.figure(figsize = (10,18));
fb['Close'].plot();
plt.show();
ms = pd.read_csv("microsoft.csv");
print(ms);
# plt.figure(10,8);
# print(ms.loc['01-01-2016':'31-12-2016']);
# plt.show();
plt.figure(figsize = (10, 8));
ms.loc['01-01-2016':'31-12-2016']['Close'].plot();
plt.show();