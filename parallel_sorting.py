import csv
import os
import time
from multiprocessing import Pool
from sorting_algorithms import quick_sort, merge_sort, bubble_sort

def parallel_sort(data_chunk, algorithm):
    # Sort the data chunk using the specified sorting algorithm
    return algorithm(data_chunk)

def read_data(file_path):
    # Function to read data from CSV files
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return [int(row[0]) for row in reader]

def write_results(file_path, algorithm_name, duration):
    # Function to write performance results to a CSV file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Check if file is empty to write header
        if file.tell() == 0:
            writer.writerow(['Algorithm', 'Duration'])  # Write header
        writer.writerow([algorithm_name, duration])  # Write algorithm name and duration

def parallel_sort_wrapper(args):
    return parallel_sort(*args)

def sort_and_measure(data_chunks, algorithm, num_processors):
    with Pool(processes=num_processors) as pool:
        # Sort the chunks in parallel and measure the total duration
        start = time.time()

        # Map the chunks to the sorting function
        tasks = [(chunk, algorithm) for chunk in data_chunks]
        sorted_chunks = pool.map(parallel_sort_wrapper, tasks)

        end = time.time()

        # Merge the sorted chunks if necessary
        # ... (This part is omitted for brevity)

        duration = end - start
        return duration

if __name__ == '__main__':
    num_processors = os.cpu_count()  # Get the number of processors
    data = read_data('datasets/dataset1.csv')  # Replace with your actual data path
    chunks = [data[i::num_processors] for i in range(num_processors)]  # Split data into chunks

    # Measure the performance of parallel QuickSort
    duration_qs = sort_and_measure(chunks, quick_sort, num_processors)
    write_results('results/performance_results.csv', 'QuickSort', duration_qs)

    # Repeat the process for MergeSort and BubbleSort
    # Add similar lines for MergeSort and BubbleSort
