graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# BFS: visit neighbours first
queue = ["A"]
visited_bfs = []

while queue:
    place = queue.pop(0)
    if place not in visited_bfs:
        visited_bfs.append(place)
        queue += graph[place]

print("BFS:", visited_bfs)

# DFS: keep following one path
stack = ["A"]
visited_dfs = []

while stack:
    place = stack.pop()
    if place not in visited_dfs:
        visited_dfs.append(place)
        stack += graph[place]

print("DFS:", visited_dfs)