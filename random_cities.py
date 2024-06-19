import random

def generate_random_cities(num_cities):
    cities = {}
    for i in range(num_cities):
        city_name = f"City_{i}"
        weight = random.randint(1, 100)
        cities[city_name] = weight
    return cities

# Example usage
num_cities = 100
cities = generate_random_cities(num_cities)
print(cities)
