import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
sample_data = np.random.normal(size=100000)  
plt.hist(sample_data)
plt.show()  #to plot histogram without axises
sbn.distplot(sample_data)
#sbn.distplot(sample_data,kde=True)   #Note:- kde=False for remove Normal Dist line


