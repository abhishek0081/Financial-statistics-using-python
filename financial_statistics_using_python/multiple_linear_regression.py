import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import scipy.stats as stats
allord =  pd.read_csv("ALLOrdinary.csv");
nikkei = pd.read_csv("Nikkei225.csv");
hsi = pd.read_csv("HSI.csv");
daxi = pd.read_csv("DAXI.csv");
cac40 = pd.read_csv("CAC40.csv");
sp500 = pd.read_csv("SP500.csv");
dji = pd.read_csv("DJI.csv");
nasdaq = pd.read_csv("nasdaq_composite.csv");
spy = pd.read_csv("SPY.csv");


###########  DATA MUNGING  #########
indicepanel = pd.DataFrame(index=spy.index);
indicepanel["spy"] = spy["Open"].shift(-1)-spy["Open"];
indicepanel["spy_lag1"] = indicepanel["spy"].shift(1);
indicepanel["sp500"]= sp500["Open"] - sp500["Open"].shift(1);
indicepanel["nasdaq"] = nasdaq["Open"] -nasdaq["Open"].shift(1);
indicepanel["dji"]= dji["Open"] - dji["Open"].shift(1);
indicepanel["cac40"]= cac40["Open"] - cac40["Open"].shift(1);
indicepanel["daxi"]= daxi["Open"] - daxi["Open"].shift(1);
indicepanel["allord"]= allord["Open"] - allord["Open"].shift(1);
indicepanel["hsi"]= hsi["Open"] - hsi["Open"].shift(1);
indicepanel["nikkei"]= nikkei["Open"] - nikkei["Open"].shift(1);
indicepanel["Price"] = spy["Open"];
print(indicepanel.head());

indicepanel = indicepanel.fillna(method="ffill");
indicepanel = indicepanel.dropna();
indicepanel.isnull().sum();
indicepanel.to_csv("indicepanel.csv");

print(indicepanel.shape)

# 2677 days of data
# 1 Response
# 9 predictoors
# 1 open of SPY

#########  DATA SPLITTING ############
Train = indicepanel.iloc[-2000:-1000,:];
Test = indicepanel.iloc[-1000:,:];
print(Train.shape,Test.shape);
sm = scatter_matrix(Train,figsize=(10,10));
plt.show();
print(Train.iloc[:,:-1].corr()["spy"]);


############  OLSE ############

formula = "spy~spy_lag1+sp500+nasdaq+dji+cac40+daxi+allord+nikkei+hsi"
lm =smf.ols(formula=formula,data=Train).fit();
print(lm.summary());

########### MULTICOLLINEARTITY ##########3
print(Train.iloc[:,:-1].corr());

####### MAKING PREDICTION ##########3
Train["PredictedY"] = lm.predict(Train);
Test["PredictedY"] = lm.predict(Test);
plt.scatter(Train["spy"],Train["PredictedY"]);
plt.show();

#########  MODEL  EVALUATION #######
def adjustedMetric(data,model,model_k,yname):
    data["yhat"]=model.predict(data);
    SST = ((data[yname] - data[yname].mean())**2).sum();
    SSR = ((data["yhat"] - data[yname].mean())**2).sum();
    SSE = ((data[yname] - data["yhat"])**2).sum()    
    r2 = SSR/SST;
    adjustedR2 = 1-(1-r2)*(data.shape[0]-1)/(data.shape[0]-model_k-1);
    RMSE = (SSE/(data.shape[0]-model_k-1))**0.5
    return adjustedR2,RMSE


print("Adjusted R2 AND RMSE on TRAIN  : ",adjustedMetric(Train,lm,9,"spy"));
print("Adjusted R2 AND RMSE on Test  : ",adjustedMetric(Test,lm,9,"spy"));

def assessTable(test, train, model, model_k, yname):
    r2test, RMSEtest = adjustedMetric(test, model, model_k, yname)
    r2train, RMSEtrain = adjustedMetric(train, model, model_k, yname)
    assessment = pd.DataFrame(index=['R2', 'RMSE'], columns=['Train', 'Test'])
    assessment['Train'] = [r2train, RMSEtrain]
    assessment['Test'] = [r2test, RMSEtest]
    return assessment


######## overfitting test  ######## 
print(assessTable(Test,Train,lm,9,"spy"));

#if RMSE and adj R^2 in train and test differ dramatically we conclude overfitting

####### Here in this data there is  no overfitting 

##############  Profit of signal -based  strategy #############33
Train["Order"] = [1 if sig>0 else -1 for sig in Train["PredictedY"] ] #predicted return of spy
Train["Profit"] = Train["spy"]*Train["Order"];

Train["Wealth"]= Train["Profit"].cumsum();
print("Total profit made in Train :",Train["Profit"].sum())


#signal Based Buy and Hold

plt.figure(figsize=(10, 10))
plt.title('Performance of Strategy in Train')
plt.plot(Train['Wealth'].values, color='green', label='Signal based strategy')
plt.plot(Train['spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()

##############  Profit of signal -based Test Data #############
Test["Order"] = [1 if sig>0 else -1 for sig in Test["PredictedY"] ] #predicted return of spy
Test["Profit"] = Test["spy"]*Test["Order"];

Test["Wealth"]= Test["Profit"].cumsum();
print("Total profit made in Train :",Test["Profit"].sum())

plt.figure(figsize=(10, 10))
plt.title('Performance of Strategy in Train')
plt.plot(Test['Wealth'].values, color='green', label='Signal based strategy')
plt.plot(Test['spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()


###########  EVALUATION  OF MODEL ###############

####  sharpe ratio  : Measures the excess return (or risk premium) per unit of deviation in an investment or a trading stategy ,typically referred to as risk.
# Sharpe ratio = mean of excess return /Sd of excess return
# SR year = sqrt(252*SR day)

Test["Return"] =  np.log(Test["Wealth"])-np.log(Test["Wealth"].shift(1));
dailyr = Test["Return"].dropna();
print("Daily sharpe ratio is ", dailyr.mean()/dailyr.std(ddof=1));
print("Yearly sharpe ratio is : ",(252**0.5)*dailyr.mean()/dailyr.std(ddof=1));

##  Maximum Drawdown : The maximum % decline in the strategy from the historical peal profit at eaxh point in time.

# drawdown  = (max -wealth)/max


### Compute the peak of wealth process

Train["Peak"] = Train["Wealth"].cummax();
Train["Drawdown"] = (Train["Peak"]-Train["Wealth"])/Train["Peak"];

Test["Peak"] = Test["Wealth"].cummax();
Test["Drawdown"] = (Test["Peak"]-Test["Wealth"])/Test["Peak"];

print("Maximum Drawdown in train is : ",Train["Drawdown"].max());
print("Maximum Drawdown in test is : ",Test["Drawdown"].max());

#######  conclusion:

# Not Overfitted

# consistent