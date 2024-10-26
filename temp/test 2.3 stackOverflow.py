import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x1 = np.random.randn(100).cumsum()
x2 = np.random.randn(100).cumsum()
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(15, 4))
sns.distplot(a=x1, kde=False, norm_hist=True, ax=ax2)
sns.distplot(a=x2, ax=ax2)
ax2.set_title('setting norm_hist=True')
plt.show()
