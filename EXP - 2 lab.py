# EXPERIMENT 2: DFS for Dependency and Reachability Analysis
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)

start = "A"
target = "G"
dfs(start)

print("EXPERIMENT 2 - DFS for Dependency and Reachability Analysis")
print("DFS Traversal:", visited)
print("Target is reachable" if target in visited else "Target is not reachable")
