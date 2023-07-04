import heapq
from Levenshtein import distance

def heuristic(node, goal):
    return distance(node, goal)

def a_star_search(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

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

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

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

path = a_star_search(graph, start_node, goal_node)

if path:
    print("Path:", ' -> '.join(path))
else:
    print("No path found.")
