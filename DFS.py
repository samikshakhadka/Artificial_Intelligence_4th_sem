def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    print(start_vertex, end=" ")

    for adjacent_vertex in graph[start_vertex]:
        if adjacent_vertex not in visited:
            dfs(graph, adjacent_vertex, visited)

# Example usage
graph = {
    0: [1, 2],  # Vertex 0 is connected to vertices 1 and 2
    1: [0, 3, 4],  # Vertex 1 is connected to vertices 0, 3, and 4
    2: [0, 4],  # Vertex 2 is connected to vertices 0 and 4
    3: [1],  # Vertex 3 is connected to vertex 1
    4: [1, 2]  # Vertex 4 is connected to vertices 1 and 2
}
start_vertex = 0

print("DFS Traversal:", end=" ")
dfs(graph, start_vertex)
