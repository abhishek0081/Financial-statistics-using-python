import pandas as pd
import numpy as np
data = pd.DataFrame();
data['population'] = [45,78,2,4,89,2,5,74,123,576,34,65,223,432,54,6,45,2,345,54,56,76,3325,6556,55,6576,4345,546,565,45,465,89];
srswor = data['population'].sample(5,replace = False);
print(srswor);
srswr = data['population'].sample(5,replace = True);
print(srswr);
print('Population size is ' ,data['population'].shape[0]);
print('Population standard deviation is ',data['population'].std(ddof = 0));
print('population variance is ',data['population'].var(ddof = 0));
print('population mean is ',data['population'].mean());
sample_length = 500;
sample_variance_collection0 = [data['population'].sample(50,replace = True).var(ddof=0) for i in range(sample_length)];
sample_variance_collection1 = [data['population'].sample(50,replace = True).var(ddof = 1) for i in range(sample_length)];
print(sample_variance_collection0);
print(sample_variance_collection1);
print('###############################');
print('population variance is ',data['population'].var(ddof=0));
print('Average of sample varicne with n is',pd.DataFrame(sample_variance_collection0)[0].mean());
print('Average of sample variance with n-1 is ',pd.DataFrame(sample_variance_collection1)[0].mean());
###  Degree of Freedom
