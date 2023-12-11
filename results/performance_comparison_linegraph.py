import pandas as pd
import matplotlib.pyplot as plt

# Read the performance data from the CSV file
data = pd.read_csv('results/performance_results.csv')  # Update with the correct file path

# Separate data for sequential and parallel execution
sequential_data = data[data['Type'] == 'Sequential']
parallel_data = data[data['Type'] == 'Parallel']

# Create a line chart for QuickSort
plt.figure(figsize=(10, 6))
plt.plot(sequential_data['Algorithm'], sequential_data['Execution Time'], label='Sequential')
plt.plot(parallel_data['Algorithm'], parallel_data['Execution Time'], label='Parallel')
plt.xlabel('Algorithm')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of Sorting Algorithms (QuickSort)')
plt.legend()
plt.grid(True)

# Save the line chart as an image (e.g., PNG)
plt.savefig('results/quick_sort_performance_line_chart.png')

# Show the line chart
plt.show()
