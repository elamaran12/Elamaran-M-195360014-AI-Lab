# EXPERIMENT 6: Map Colouring Problem Using CSP (Backtracking)

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}
colors = ["Red", "Green", "Blue"]
assignment = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve(regions):
    if len(assignment) == len(regions):
        return True

    region = next(r for r in regions if r not in assignment)
    for color in colors:
        if is_safe(region, color):
            assignment[region] = color
            if solve(regions):
                return True
            del assignment[region]  # backtrack
    return False

regions = list(graph.keys())
print("EXPERIMENT 6 - Map Colouring Using CSP")
if solve(regions):
    for region in regions:
        print(f"Region {region}: {assignment[region]}")
else:
    print("No valid colouring found")
