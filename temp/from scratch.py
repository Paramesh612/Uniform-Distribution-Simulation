import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sample=[np.random.normal(size=10) for i in range(5)]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 4))

plt.hist(sample,color='skyblue')
sns.displot(sample,kde=True ,color='darkred',ax=ax2 )
plt.show()