import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

def apply_CLT(sample_data, sample_size, total_samples):
    sample_mean = []
    for a in range(total_samples):
        sample = np.random.choice(sample_data, size=sample_size)
        mean = np.mean(sample)
        sample_mean.append(mean)
     
    return sample_mean

def plot_distribution(distribution_type, sample_size=30, total_samples=1000, initial_sample_size=700):
    if distribution_type == "uniform":
        sample_data = np.random.uniform(size=initial_sample_size)
    elif distribution_type == "binomial":
        sample_data = np.random.binomial(n=10, p=0.5, size=initial_sample_size)
    elif distribution_type == "poisson":
        sample_data = np.random.poisson(lam=5, size=initial_sample_size)
    elif distribution_type == "exponential":
        sample_data = np.random.exponential(scale=1.0, size=initial_sample_size)
    elif distribution_type == "geometric":
        sample_data = np.random.geometric(p=0.3, size=initial_sample_size)
    else:
        print("Invalid distribution type")
        return

    # Create a 1x2 subplot grid
    plt.subplot(1, 2, 1)
    sbn.distplot(sample_data)
    plt.title(f"Before Applying CLT ({distribution_type.capitalize()} Distribution)")

    plt.subplot(1, 2, 2)
    sbn.distplot(apply_CLT(sample_data, sample_size, total_samples))
    plt.title(f"After Applying CLT ({distribution_type.capitalize()} Distribution)")

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plots
    plt.show()

# Example usage:
distribution_type = input("Enter distribution type (uniform, binomial, poisson, exponential, geometric): \n").lower()
plot_distribution(distribution_type)
