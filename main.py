# main.py
from parallel_sorting import parallel_sort
from sorting_algorithms import quick_sort, merge_sort, bubble_sort
from performance_metrics import measure_time
import csv


# Function to read dataset from CSV
def read_dataset(file_path):


# Implementation as before...

# Function to write results to CSV
def write_results(results, file_path):


# Implementation as before...

def run_sequential_sorts(data):
    results = []
    for sort_func in [quick_sort, merge_sort, bubble_sort]:
        time_taken = measure_time(sort_func, data[:])  # Pass a copy to avoid in-place sorting
        results.append((sort_func.__name__, 'Sequential', time_taken))
    return results


def run_parallel_sort(data):
    time_taken = measure_time(parallel_sort, data[:])  # Pass a copy since parallel sort will sort in-place
    return ('ParallelSort', 'Parallel', time_taken)


if __name__ == '__main__':
    data = read_dataset('datasets/dataset_1.csv')

    # Run and collect results for sequential sorting
    sequential_results = run_sequential_sorts(data)

    # Run and collect results for parallel sorting
    parallel_result = run_parallel_sort(data)

    # Combine results
    all_results = sequential_results + [parallel_result]

    # Write the combined results to CSV
    write_results(all_results, 'results/performance_results.csv')
