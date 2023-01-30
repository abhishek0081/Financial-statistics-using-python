from numpy.core.numeric import indices
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import scipy.stats as stats


housing = pd.read_csv("housing.csv",index_col=0);
print(housing.head());
b0 = 1
b1 = 0.4;
housing['GuessResponse'] = b0 +b1*housing["RM"];
housing['ObserveError'] = housing["MEDV"];
housing["GuessResponse"];
indices = [7,20,100];
print(housing["ObserveError"].loc[indices]);
print("Sum of sqaured error is ", (housing["ObserveError"]**2).sum());
################  OLSE ######################

model = smf.ols(formula='MEDV~LSTAT',data=housing).fit();
b0 = model.params[0];
b1 = model.params[-1];
housing["BestResponse"] = b0 +b1*housing["LSTAT"];

####  plotting######
plt.title('Sum of sqaured error is {}'.format((((housing['ObserveError'])**2)).sum()))
# plt.figure(figsize=(10,10));
plt.scatter(housing['RM'],housing["MEDV"],color="g",label="real");
# plt.scatter(housing['RM'],housing["MEDV"],color="b",label="model");
plt.scatter(housing['RM'],housing["GuessResponse"],color="red");
plt.scatter(housing['RM'],housing["BestResponse"],color="yellow");
plt.ylabel("MEDV/$1000");
plt.xlabel("RM/number");
plt.legend();
plt.xlim(np.min(housing["RM"])-2,np.max(housing["RM"])+2);
plt.xlim(np.min(housing["MEDV"])-2,np.max(housing["MEDV"])+2)

plt.show();
plt.scatter(housing['RM'], housing['MEDV'], color='g', label='Observed')
plt.plot(housing['RM'], housing['GuessResponse'], color='red', label='GuessResponse')
plt.plot(housing['RM'], housing['BestResponse'], color='yellow', label='BestResponse')
plt.legend()
plt.xlim(housing['RM'].min()-2, housing['RM'].max()+2)
plt.ylim(housing['MEDV'].min()-2, housing['MEDV'].max()+2)
plt.show();
print(model.summary());

################  INDEPENDENCE  ###################
housing["error"] =housing['MEDV']  - housing["BestResponse"];
plt.figure(figsize=(15,8));
plt.title("Residuals vs order");
plt.plot(housing.index,housing["error"],color = "magenta");
plt.axhline(y=0,color="red");
plt.show();
## assumption of independence violated by durbin watson test as it is showing +ve correlation

############  NORMALITY ###################3

z = (housing["error"]-housing["error"].mean())/housing["error"].std(ddof=1);
stats.probplot(z,dist="norm",plot = plt);
plt.title("NORMAL Q-Q PLOT");
plt.show();

## normality assimption holds

################# EQUALITY OF VARIANCE #################33

housing.plot(kind = 'scatter',x = "RM", y ="error",figsize=(15,8),color = "crimson");
plt.title("Residuals vs predictor");
plt.axhline(y=0,color="cyan");
plt.show();

######## asssumption of equal variance is violated as variance is smaller for larger RM


