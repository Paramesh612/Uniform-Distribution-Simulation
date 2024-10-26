import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

def apply_CLT(sample_data,sample_size,total_samples):
  sample_mean = []
  for a in range(total_samples):  #iterating for total no of samples for choosing samples and their mean
    sample = np.random.choice(sample_data, size = sample_size)    #Note:- replace=False for with-out replacement
    mean = np.mean(sample)      #Finding mean of random chose samples using numpy
    sample_mean.append(mean)     
     
  return sample_mean

sample_data = np.random.uniform(size=100)

sbn.distplot(sample_data)   #distribution plot  
plt.title("Before Applying Central Limit Theorem (Uniform Distribution)")
plt.show()
#Appling CLT on sample data. Funtion = apply_CLT(sample_data,sample_size,total_samples)
sbn.distplot( apply_CLT(sample_data,30,1000) )
plt.title("After Applying Central Limit Theorem")
plt.show()

