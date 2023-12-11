# main.py
from parallel_sorting import sort_and_measure  # This is the corrected import
from sorting_algorithms import quick_sort, merge_sort, bubble_sort
from performance_metrics import measure_time
import csv
import os

# Function to read dataset from CSV
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return [int(row[0]) for row in reader]

# Function to write results to CSV
def write_results(file_path, results):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Algorithm', 'Type', 'Execution Time'])
        writer.writerows(results)

def run_sequential_sorts(data):
    results = []
    for sort_func in [quick_sort, merge_sort, bubble_sort]:
        time_taken = measure_time(sort_func, data[:])  # Pass a copy to avoid in-place sorting
        results.append((sort_func.__name__, 'Sequential', time_taken))
    return results

def run_parallel_sort(data_chunks, algorithm, num_processors):
    # Measure the time taken by the parallel sorting algorithm
    time_taken = sort_and_measure(data_chunks, algorithm, num_processors)
    return (algorithm.__name__, 'Parallel', time_taken)

if __name__ == '__main__':
    num_processors = os.cpu_count()
    data = read_dataset('datasets/dataset_2.csv')
    chunks = [data[i::num_processors] for i in range(num_processors)]

    # Run and collect results for sequential sorting
    sequential_results = run_sequential_sorts(data)

    # Prepare a list to collect all results
    all_results = sequential_results

    # Run and collect results for parallel sorting using each algorithm
    for algorithm in [quick_sort, merge_sort, bubble_sort]:
        parallel_result = run_parallel_sort(chunks, algorithm, num_processors)
        all_results.append(parallel_result)

    # Write the combined results to CSV
    write_results('results/performance_results.csv', all_results)
