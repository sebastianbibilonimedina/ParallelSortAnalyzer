import pandas as pd
import matplotlib.pyplot as plt

# Define the full path to the CSV file
csv_file_path = 'results/performance_results.csv'

# Load data from the CSV file
data = pd.read_csv(csv_file_path)

# Separate data for sequential and parallel execution
sequential_data = data[data['Type'] == 'Sequential']
parallel_data = data[data['Type'] == 'Parallel']

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(sequential_data['Algorithm'], sequential_data['Execution Time'], label='Sequential', marker='o')
plt.scatter(parallel_data['Algorithm'], parallel_data['Execution Time'], label='Parallel', marker='x')
plt.xlabel('Algorithm')
plt.ylabel('Execution Time')
plt.title('Performance Comparison: Sequential vs. Parallel Sorting Algorithms')
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Save the scatter plot as a PNG file
output_file_path = 'results/performance_comparison.png'
plt.savefig(output_file_path)

# Display the plot (optional)
plt.show()
