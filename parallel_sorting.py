import csv
import os
import time
from multiprocessing import Pool
from sorting_algorithms import quick_sort, merge_sort, bubble_sort

def read_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return [int(row[0]) for row in reader]

def write_results(file_path, algorithm_name, duration):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Algorithm', 'Type', 'Duration'])
        writer.writerow([algorithm_name, 'Parallel', duration])

def parallel_sort(data_chunk, algorithm):
    return algorithm(data_chunk)

def parallel_sort_wrapper(args):
    return parallel_sort(*args)

def chunk_data(data, num_chunks):
    chunk_size = len(data) // num_chunks
    return (data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks))

def efficient_merge(sorted_chunks, algorithm):
    if algorithm == merge_sort:
        # Implement a more efficient multi-way merge for merge_sort
        # Placeholder for the multi-way merge implementation
        return sorted_chunks
    else:
        # For other algorithms, simply concatenate and sort
        return sorted(sum(sorted_chunks, []), key=lambda x: x)

def sort_and_measure(data, algorithm, num_processors):
    data_chunks = list(chunk_data(data, num_processors))

    with Pool(processes=num_processors) as pool:
        start = time.time()
        tasks = [(chunk, algorithm) for chunk in data_chunks]
        sorted_chunks = pool.map(parallel_sort_wrapper, tasks)
        sorted_data = efficient_merge(sorted_chunks, algorithm)
        end = time.time()

        duration = end - start
        return duration

if __name__ == '__main__':
    num_processors = os.cpu_count()
    data = read_data('datasets/dataset1.csv')

    # Testing QuickSort and MergeSort
    for algorithm in [quick_sort, merge_sort]:
        duration = sort_and_measure(data, algorithm, num_processors)
        write_results('results/performance_results.csv', algorithm.__name__, duration)
