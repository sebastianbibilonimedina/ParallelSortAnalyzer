import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Dataset': ['Dataset 1', 'Dataset 1', 'Dataset 1', 'Dataset 1', 'Dataset 1', 'Dataset 1',
                'Dataset 2', 'Dataset 2', 'Dataset 2', 'Dataset 2', 'Dataset 2', 'Dataset 2',
                'Dataset 3', 'Dataset 3', 'Dataset 3', 'Dataset 3', 'Dataset 3', 'Dataset 3'],
    'Algorithm': ['Quick Sort', 'Merge Sort', 'Bubble Sort', 'Quick Sort', 'Merge Sort', 'Bubble Sort',
                  'Quick Sort', 'Merge Sort', 'Bubble Sort', 'Quick Sort', 'Merge Sort', 'Bubble Sort',
                  'Quick Sort', 'Merge Sort', 'Bubble Sort', 'Quick Sort', 'Merge Sort', 'Bubble Sort'],
    'Type': ['Sequential', 'Sequential', 'Sequential', 'Parallel', 'Parallel', 'Parallel',
             'Sequential', 'Sequential', 'Sequential', 'Parallel', 'Parallel', 'Parallel',
             'Sequential', 'Sequential', 'Sequential', 'Parallel', 'Parallel', 'Parallel'],
    'Execution Time': [0.0025, 0.0028, 0.0873, 0.6943, 0.4486, 0.4410,
                       0.0271, 0.0366, 9.3770, 0.5815, 0.6023, 0.5360,
                       0.1952, 0.3796, 244.1401, 0.5915, 0.4270, 0.4465]
}

# Create DataFrame
df = pd.DataFrame(data)

# Preparing the data for the plot
pivot_df = df.pivot(index='Algorithm', columns=['Dataset', 'Type'], values='Execution Time')

# Creating the bar plot
ax = pivot_df.plot(kind='bar', figsize=(15, 7), logy=True)

# Customizing the plot
plt.title('Performance Comparison of Sorting Algorithms')
plt.ylabel('Execution Time (seconds) - Log Scale')
plt.xlabel('Algorithm')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Setting a logarithmic scale for the y-axis
ax.set_yscale('log')
ax.set_yticks([0.001, 0.01, 0.1, 1, 10, 100, 1000])
ax.get_yaxis().set_major_formatter(plt.ScalarFormatter())


# Show the plot
plt.show()
