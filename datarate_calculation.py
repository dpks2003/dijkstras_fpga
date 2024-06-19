import random
import pickle
import time

def generate_random_cities(num_cities):
    cities = {}
    for i in range(num_cities):
        city_name = f"City_{i}"
        weight = random.randint(1, 100)
        cities[city_name] = weight
    return cities

# Step 1: Measure Data Size Per Call
num_cities = 100
data = generate_random_cities(num_cities)
data_size = len(pickle.dumps(data))
print(f"Data size per call: {data_size} bytes")

# Step 2: Measure Execution Time with Multiple Iterations
iterations = 1000  # Increase the number of iterations
start_time = time.perf_counter()
for _ in range(iterations):
    generate_random_cities(num_cities)
end_time = time.perf_counter()

execution_time = (end_time - start_time) / iterations
print(f"Execution time per call: {execution_time} seconds")

# Step 3: Calculate Data Rate
data_rate = data_size / execution_time
print(f"Data rate: {data_rate} bytes per second")
