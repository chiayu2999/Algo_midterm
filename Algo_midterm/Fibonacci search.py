#method3_fibonacci search
import random
import time

# Function for Fibonacci search
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


# Generate random list of integers
n = 10
S = random.sample(range(1, 101), n)

# Generate random integer
x = random.randint(1, 101)

# Execute Fibonacci search and record execution times
total_time = 0
num_iterations = 5
for i in range(num_iterations):
    start_time = time.time()
    index = fibonacci_search(S, x)
    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

# Calculate mean execution time
mean_time = total_time / num_iterations

# Print results
print("S:", S)
print("x:", x)
print("Fibonacci search index:", index)
print("Mean execution time:", mean_time)

# Repeat process for n = 10, 20, 30, ..., up to 1000
for n in range(10, 1010, 10):
    # Generate random list of integers
    S = random.sample(range(1, 10001), n)

    # Generate random integer
    x = random.randint(1, 10001)

    # Execute Fibonacci search and record execution times
    total_time = 0
    num_iterations = 5
    for i in range(num_iterations):
        start_time = time.time()
        index = fibonacci_search(S, x)
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

    # Calculate mean execution time
    mean_time = total_time / num_iterations

    # Print results
    print("n:", n)
    print("Mean execution time:", mean_time)
