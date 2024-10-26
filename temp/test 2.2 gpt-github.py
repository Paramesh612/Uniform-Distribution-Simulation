import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate random data
sample_data = np.random.poisson(size=100000)

# Create a matplotlib figure and axis
fig, ax = plt.subplots()

# Plot histogram on the specified axis
sns.histplot(sample_data, bins=30, color='skyblue', kde=False, ax=ax)  #<TAG>

# Plot KDE along with histogram on the same axis
sns.kdeplot(sample_data, color='darkred', ax=ax) #<TAG>

# Set titles and labels
plt.title('Histogram with KDE')
plt.xlabel('Values')
plt.ylabel('Frequency/Density')

# Show the plot
plt.show()

def apply_CLT(sample_data,sample_size,total_samples):
  sample_mean = []
  for a in range(total_samples):  #iterating for total no of samples for choosing samples and their mean
    sample = np.random.choice(sample_data, size = sample_size)    #Note:- replace=False for with-out replacement
    mean = np.mean(sample)      #Finding mean of random chose samples using numpy
    sample_mean.append(mean)     
     
  return sample_mean