from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque()
    visited.add(start_vertex)
    queue.append(start_vertex)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=" ")

        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited:
                visited.add(adjacent_vertex)
                queue.append(adjacent_vertex)

# Define the graph
graph = {
    0: [1, 2],  # Vertex 0 is connected to vertices 1 and 2
    1: [0, 3, 4],  # Vertex 1 is connected to vertices 0, 3, and 4
    2: [0, 4],  # Vertex 2 is connected to vertices 0 and 4
    3: [1],  # Vertex 3 is connected to vertex 1
    4: [1, 2]  # Vertex 4 is connected to vertices 1 and 2
}

start_vertex = 0

print("BFS Traversal:", end=" ")
bfs(graph, start_vertex)
