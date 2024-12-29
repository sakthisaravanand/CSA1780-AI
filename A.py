import heapq

# A* Algorithm
class AStar:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        # Directions to move: up, down, left, right
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Heuristic function: Manhattan Distance
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Check if a position is valid (in bounds and not a wall)
    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 1

    # Reconstruct the path from the goal to the start
    def reconstruct_path(self, came_from):
        path = []
        current = self.goal
        while current != self.start:
            path.append(current)
            current = came_from[current]
        path.append(self.start)
        path.reverse()
        return path

    # A* algorithm
    def a_star(self):
        # Open list (priority queue), Closed list, came_from map
        open_list = []
        heapq.heappush(open_list, (0 + self.heuristic(self.start, self.goal), 0, self.start))  # (f, g, position)
        g_costs = {self.start: 0}
        came_from = {}

        while open_list:
            _, g, current = heapq.heappop(open_list)

            if current == self.goal:
                return self.reconstruct_path(came_from)

            # For each neighbor
            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])

                if self.is_valid(neighbor[0], neighbor[1]) and neighbor not in came_from:
                    tentative_g_cost = g + 1  # Each step has cost of 1
                    if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                        g_costs[neighbor] = tentative_g_cost
                        f_cost = tentative_g_cost + self.heuristic(neighbor, self.goal)
                        heapq.heappush(open_list, (f_cost, tentative_g_cost, neighbor))
                        came_from[neighbor] = current

        return None  # No path found

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    astar = AStar(start, goal, grid)
    path = astar.a_star()

    if path:
        print("Path found:", path)
    else:
        print("No path found")
