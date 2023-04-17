#method1_linear search
import random
import time

# Define linear search algorithm
def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

# Initialize variables
times_linear = []
n_values = range(10, 1010, 10)
num_trials = 5
num_iterations = 100

# Perform search algorithm and record execution times
for n in n_values:
    print(f"Running for n = {n}")
    total_time_linear = 0
    for _ in range(num_iterations):
        # Generate list of integers and target integer
        S = random.sample(range(1, n*10), n)
        x = random.randint(1, n*10)

        # Execute linear search and record time
        start_time = time.time()
        for _ in range(num_trials):
            linear_search(S, x)
        total_time_linear += (time.time() - start_time) / num_trials

    # Record average execution time for linear search algorithm
    times_linear.append(total_time_linear / num_iterations)

# Print results
print("Results:")
for i in range(len(n_values)):
    print(f"n = {n_values[i]}: Linear Search = {times_linear[i]:.6f}s")
