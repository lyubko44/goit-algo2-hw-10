import random
import time
import matplotlib.pyplot as plt
import numpy as np

def partition(arr, low, high, pivot_index):
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort_helper(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        pivot_pos = partition(arr, low, high, pivot_index)
        
        randomized_quicksort_helper(arr, low, pivot_pos - 1)
        randomized_quicksort_helper(arr, pivot_pos + 1, high)

def deterministic_quicksort_helper(arr, low, high):
    if low < high:
        pivot_index = high
        pivot_pos = partition(arr, low, high, pivot_index)
        
        deterministic_quicksort_helper(arr, low, pivot_pos - 1)
        deterministic_quicksort_helper(arr, pivot_pos + 1, high)

def randomized_quick_sort(arr):
    arr_copy = arr.copy()
    randomized_quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def deterministic_quick_sort(arr):
    arr_copy = arr.copy()
    deterministic_quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def measure_sorting_time(sort_func, arr, num_runs=5):
    times = []
    for _ in range(num_runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / num_runs

def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    random_times = []
    deterministic_times = []
    
    for size in sizes:
        arr = [random.randint(1, 1000000) for _ in range(size)]
        
        random_time = measure_sorting_time(randomized_quick_sort, arr)
        random_times.append(random_time)
        
        deterministic_time = measure_sorting_time(deterministic_quick_sort, arr)
        deterministic_times.append(deterministic_time)
        
        print(f"\nРозмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {random_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд")
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, random_times, 'b-o', label='Рандомізований QuickSort')
    plt.plot(sizes, deterministic_times, 'r-o', label='Детермінований QuickSort')
    
    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння ефективності алгоритмів QuickSort')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('quicksort_comparison.png')
    plt.close()

if __name__ == "__main__":
    main() 