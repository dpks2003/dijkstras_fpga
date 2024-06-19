# complete algorithm implementaion in python 
# I have used chat gpt for the visualization function using matplotlib but it works well 
# there for it is not optimized for the timing 

import random
import matplotlib.pyplot as plt

def generate_random_graph(num_cities):
    cities = [f"City_{i}" for i in range(1, num_cities + 1)]
    graph = {city: {} for city in cities}
    
    # Create random connections with random weights
    for i in range(num_cities):
        num_connections = random.randint(1, 10)  # Adjust connection density as needed
        for _ in range(num_connections):
            neighbor = random.choice(cities)
            while neighbor == cities[i] or neighbor in graph[cities[i]]:
                neighbor = random.choice(cities)
            weight = random.randint(50, 500)  # Random weight between 50 and 500
            graph[cities[i]][neighbor] = weight
            graph[neighbor][cities[i]] = weight  # Assuming bidirectional connections
    
    return graph

def dijkstra(graph, start, end):
    
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
  
    priority_queue = [(0, start)]
 
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = min(priority_queue, key=lambda x: x[0])
        priority_queue.remove((current_distance, current_node))
        
        # If we reach the end node, we can build the shortest path
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return path[::-1], distances[end]
        
        # Skip processing if the current distance is greater than the recorded distance
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Check if neighbor is present in distances dictionary
            if neighbor not in distances:
                continue
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                priority_queue.append((distance, neighbor))
    
    return None, float('infinity')

def visualize_graph(graph, positions, path=None):
    plt.figure(figsize=(12, 9))
    
    # Draw edges
    for city, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            x_values = [positions[city][0], positions[neighbor][0]]
            y_values = [positions[city][1], positions[neighbor][1]]
            plt.plot(x_values, y_values, 'gray', linestyle='--')
            mid_x = (positions[city][0] + positions[neighbor][0]) / 2
            mid_y = (positions[city][1] + positions[neighbor][1]) / 2
            plt.text(mid_x, mid_y, str(weight), fontsize=8, ha='center', color='gray')
    
    # Draw nodes
    for city, (x, y) in positions.items():
        plt.scatter(x, y, s=100, color='lightblue')
        plt.text(x, y, city, fontsize=10, ha='right', color='black')
    
    # Highlight the shortest path if provided
    if path:
        path_edges = list(zip(path, path[1:]))
        for start, end in path_edges:
            x_values = [positions[start][0], positions[end][0]]
            y_values = [positions[start][1], positions[end][1]]
            plt.plot(x_values, y_values, 'blue', linewidth=2)
    
    plt.title("Random Graph Visualization of Cities with Shortest Path Highlighted")
    plt.axis('off')
    plt.show()

def main():
    # Generate random graph with around 100 cities
    num_cities = 50
    graph = generate_random_graph(num_cities)
    
    # Generate random positions for cities on a 2D plane
    positions = {city: (random.uniform(0, 1000), random.uniform(0, 1000)) for city in graph}
    
    # Visualize the graph initially without any path highlighted
    visualize_graph(graph, positions)
    
    # Prompt user to enter start and end cities
    start_city = input("Enter the start city: ")
    end_city = input("Enter the end city: ")
    
    # Ensure user input cities are in the graph
    if start_city in graph and end_city in graph:
        # Find shortest path using Dijkstra's algorithm
        path, distance = dijkstra(graph, start_city, end_city)
        if path:
            print(f"Shortest path from {start_city} to {end_city} is {path} with distance {distance}")
            # Visualize the graph with the shortest path highlighted
            visualize_graph(graph, positions, path)
        else:
            print(f"No path found from {start_city} to {end_city}")
    else:
        print("One of the specified cities is not in the graph.")

# Run the main function
if __name__ == "__main__":
    main()
