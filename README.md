# Probability and Statistics Simulations

This project demonstrates the simulation of various probability distributions, the application of the Central Limit Theorem (CLT), and the transformation of random variables using Python. The visualizations are generated using Matplotlib and Seaborn.

## Features

1. **Uniform Distribution Simulation**: Visualize the uniform distribution and observe the effects of the Central Limit Theorem.
2. **Central Limit Theorem**: Sample means from different distributions to illustrate how the distribution of the sample mean approaches a normal distribution.
3. **Transformation of Random Variables**: Analyze the transformation of random variables and compute their joint and marginal probability density functions (PDFs).

## Requirements

To run this project, ensure you have the following Python packages installed:

- numpy
- matplotlib
- seaborn
- sympy

You can install the required packages using pip:

```bash
pip install numpy matplotlib seaborn sympy
```

## Code Overview

### Distribution Simulation and CLT Application

The main functionality for simulating distributions and applying the Central Limit Theorem is defined in the `plot_distribution` function. This function accepts a distribution type and generates visualizations before and after applying the CLT.

### Random Variable Transformation

The transformation of random variables is handled in a separate code section that utilizes SymPy for symbolic mathematics. The code computes the Jacobian matrix and derives the joint and marginal PDFs for the transformed variables.

### Example Usage

1. **Run the Distribution Simulation**:

   Execute the following command in your terminal:

   ```bash
   python your_script.py
   ```

   You will be prompted to enter a distribution type (options include uniform, binomial, poisson, exponential, geometric).

2. **Transform Random Variables**:

   The script will also ask for two equations, a joint PDF, and limits for integration to compute the joint and marginal PDFs of the transformed variables.

## Visualizations

The generated plots include:

- Distribution plots for the selected distribution.
- Distribution of sample means before and after applying the Central Limit Theorem.
- Contour plots for the joint PDFs of the original and transformed variables.

## Conclusion

This project provides a hands-on approach to understanding fundamental concepts in probability and statistics. The visualizations help illustrate complex ideas such as the Central Limit Theorem and the transformation of random variables.

For any questions or suggestions, feel free to open an issue or contact me.
