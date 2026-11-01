import heapq

# EXPERIMENT 4: A* Search for Intelligent Route Planning
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 5)],
    "E": [("G", 2)],
    "F": [("G", 2)],
    "G": []
}

heuristic = {
    "A": 7, "B": 6, "C": 5,
    "D": 4, "E": 2, "F": 2, "G": 0
}

def astar(start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)

        if g != best_cost.get(node):
            continue

        if node == goal:
            return path, g

        for neighbor, edge_cost in graph[node]:
            new_g = g + edge_cost
            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float("inf")

path, cost = astar("A", "G")
print("EXPERIMENT 4 - A* Search for Intelligent Route Planning")
print("Shortest path:", path)
print("Total cost:", cost)
