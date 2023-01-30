import pandas as pd
import matplotlib.pyplot as plt 
from pandas.io.parsers import read_csv
from pandas.plotting import scatter_matrix
housing = read_csv("housing.csv",index_col=0);
print(housing.head());
print(housing.corr());
sm = scatter_matrix(housing,figsize=(10,10));
plt.show();
