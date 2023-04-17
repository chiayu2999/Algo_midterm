#linechart
import random
import time
import matplotlib.pyplot as plt

# Linear search algorithm
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Fibonacci search algorithm
def fibonacci_search(arr, x):
    # Initialize Fibonacci numbers
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

    # Find the smallest Fibonacci number greater than or equal to the length of the array
    while fib3 < len(arr):
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2

    # Index of the smallest element in the remaining sequence
    index = -1

    # Perform search
    while fib3 > 1:
        # Determine the index to compare
        i = min(index + fib1, len(arr)-1)

        # If x is greater than the element at the index, cut the subarray after i+1 and set new indices
        if arr[i] < x:
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
            index = i
        # If x is smaller than the element at the index, cut the subarray before i and set new indices
        elif arr[i] > x:
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2
        # If x is found, return the index
        else:
            return i

    # If element not found, return -1
    if fib2 and index < len(arr)-1 and arr[index+1] == x:
        return index+1
    return -1

# Generate data for line chart
n_values = list(range(100, 10001, 100))
linear_times = []
binary_times = []
fibonacci_times = []

for n in n_values:
    arr = random.sample(range(n*10), n)
    x = random.randint(0, n*10)
    
    # Linear search
    linear_total_time = 0
    for i in range(5):
        start_time = time.time()
        linear_search(arr, x)
        end_time = time.time()
        linear_total_time += (end_time - start_time)
    linear_avg_time = linear_total_time / 5
    linear_times.append(linear_avg_time)
    
    # Binary search
    binary_total_time = 0
    for i in range(5):
        start_time = time.time()
        binary_search(arr, x)
        end_time = time.time()
        binary_total_time += (end_time - start_time)
    binary_avg_time = binary_total_time / 5
    binary_times.append(binary_avg_time)
    
    # Fibonacci search
    fibonacci_total_time = 0
    for i in range(5):
        start_time = time.time()
        fibonacci_search(arr, x)
        end_time = time.time()
        fibonacci_total_time += (end_time - start_time)
    fibonacci_avg_time = fibonacci_total_time / 5
    fibonacci_times.append(fibonacci_avg_time)

# Plot line chart
plt.plot(n_values, linear_times, label='Linear')
plt.plot(n_values, binary_times, label='Binary')
plt.plot(n_values, fibonacci_times, label='Fibonacci')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Search Algorithm Comparison')
plt.legend()
plt.show()
