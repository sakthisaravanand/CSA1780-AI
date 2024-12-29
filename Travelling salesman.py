import itertools
import math

# Function to calculate the distance between two cities (Euclidean distance)
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Function to calculate the total distance of a given route
def calculate_route_distance(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i+1]])
    total_distance += calculate_distance(cities[route[-1]], cities[route[0]])  # Return to the starting point
    return total_distance

# Travelling Salesman Problem Brute Force Approach
def travelling_salesman_bruteforce(cities):
    n = len(cities)
    # Generate all possible routes (permutations)
    all_routes = itertools.permutations(range(n))
    
    # Initialize the shortest distance as infinity
    shortest_distance = float('inf')
    shortest_route = None
    
    # Check all permutations to find the one with the minimum distance
    for route in all_routes:
        route_distance = calculate_route_distance(route, cities)
        if route_distance < shortest_distance:
            shortest_distance = route_distance
            shortest_route = route
    
    # Return the shortest route and its distance
    return shortest_route, shortest_distance

# Example usage
if __name__ == "__main__":
    # Define the cities as a list of (x, y) coordinates
    cities = [
        (0, 0),   # City 0
        (1, 2),   # City 1
        (2, 4),   # City 2
        (3, 1),   # City 3
        (4, 3)    # City 4
    ]
    
    shortest_route, shortest_distance = travelling_salesman_bruteforce(cities)
    
    print("Shortest route:", shortest_route)
    print("Shortest distance:", shortest_distance)
