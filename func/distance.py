import numpy as np


# Function to calculate Euclidean distance between two points
def distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Function to calculate the distance matrix
def calculate_distance_matrix(locations):
    num_locations = len(locations)
    distance_matrix = np.zeros((num_locations, num_locations), dtype=np.float64)

    for i in range(num_locations):
        for j in range(num_locations):
            x1, y1 = locations[i]
            x2, y2 = locations[j]
            distance_matrix[i, j] = distance(x1, y1, x2, y2)

    return distance_matrix


# Function to calculate and display distances
def calculate_and_display_distances(routes, distance_matrix):
    """Calculate and display the distances of the routes."""
    total_distance = 0
    truck_distances = []

    for i, route in enumerate(routes):
        truck_distance = 0
        for j in range(len(route) - 1):
            truck_distance += distance_matrix[route[j]][route[j + 1]]
        truck_distances.append(truck_distance)
        total_distance += truck_distance
        routes[i] = list(map(int, route))
        print(f"Truck {i+1} route: {routes[i]}, Distance: {truck_distance:.2f}")

    print(f"Total cumulative distance: {total_distance:.2f}")
    return truck_distances, total_distance


def calculate_total_distance(route, distance_matrix):
    """Calculate the total distance of a route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    return total_distance
