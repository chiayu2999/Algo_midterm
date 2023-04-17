#method2_binary search
import random
import time

# Define binary search algorithm
def binary_search(S, x):
    left, right = 0, len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Initialize variables
times_binary = []
n_values = range(10, 1010, 10)
num_trials = 5
num_iterations = 100

# Perform binary search and record execution times
for n in n_values:
    print(f"Running for n = {n}")
    total_time_binary = 0
    for _ in range(num_iterations):
        # Generate list of integers and target integer
        S = random.sample(range(1, n*10), n)
        x = random.randint(1, n*10)

        # Execute binary search and record time
        start_time = time.time()
        for _ in range(num_trials):
            binary_search(S, x)
        total_time_binary += (time.time() - start_time) / num_trials

    # Record average execution times for binary search
    times_binary.append(total_time_binary / num_iterations)

# Print results
print("Results:")
for i in range(len(n_values)):
    print(f"n = {n_values[i]}: Binary Search = {times_binary[i]:.6f}s")
