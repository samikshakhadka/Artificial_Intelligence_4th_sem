import heapq

def heuristic(node, goal):
    # Define your heuristic function here
    # It should estimate the cost from 'node' to 'goal'
    pass

def gbfs_search(graph, start, goal):
    open_list = [(heuristic(start, goal), start)]
    came_from = {}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))

    return None  # No path found

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2},
    'C': {'A': 3, 'D': 6},
    'D': {'B': 2, 'C': 6, 'E': 8},
    'E': {'D': 8, 'F': 4},
    'F': {'E': 4, 'G': 9},
    'G': {'F': 9}
}

start_node = 'A'
goal_node = 'G'

path = gbfs_search(graph, start_node, goal_node)

if path:
    print("Path:", ' -> '.join(path))
else:
    print("No path found.")
