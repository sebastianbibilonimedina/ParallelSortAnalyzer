# main.py
from parallel_sorting import parallel_sort
from performance_metrics import measure_time
import csv
import os

# Function to read dataset from CSV
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        return [int(row[0]) for row in reader]

# Function to write results to CSV
def write_results(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Algorithm', 'Execution Time'])
        for result in results:
            writer.writerow(result)

if __name__ == '__main__':
    # Example for reading a dataset and running parallel sort
    data = read_dataset('datasets/dataset_1.csv')
    execution_time = measure_time(parallel_sort, data)
    # Store the results
    results = [('ParallelSort', execution_time)]
    write_results(results, 'results/performance_results.csv')
