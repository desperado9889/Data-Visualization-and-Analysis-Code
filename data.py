import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(0)
data = np.random.randn(100, 2)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Extract columns of data
variable1, variable2 = data[:, 0], data[:, 1]

# Bar chart for mean and median for Variable 1 and Variable 2
variables = [variable1, variable2]
labels = ['Mean', 'Median']

for i, var in enumerate(variables):
    axes[0, 0].bar(labels, [np.mean(var), np.median(var)], color=['blue', 'green'][i], alpha=0.7, label=f'Variable {i+1}')

axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Heatmap for correlation analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# Histograms for variables
axes[1, 0].hist([variable1, variable2], bins=15, color=['blue', 'green'], alpha=0.7, label=['Variable 1', 'Variable 2'])
axes[1, 0].legend()
axes[1, 0].set_title('Histograms of Variables')

# Scatter plot of Variable 1 vs Variable 2
axes[1, 1].scatter(variable1, variable2, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot: Variable 1 vs Variable 2')

# Adjust layout and display plot
plt.tight_layout()
plt.show()

