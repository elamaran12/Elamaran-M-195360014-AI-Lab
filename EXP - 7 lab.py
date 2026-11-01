# EXPERIMENT 7: Implementing the Minimax Algorithm
# Example game tree: root MAX, next level MIN, leaves are scores.

tree = [
    [3, 5],
    [6, 9],
    [1, 2],
    [0, -1]
]

def minimax(values, maximizing):
    if all(not isinstance(item, list) for item in values):
        return max(values) if maximizing else min(values)

    child_values = [minimax(child, not maximizing) for child in values]
    return max(child_values) if maximizing else min(child_values)

# Root is MAX; each pair of leaves is evaluated by MIN.
root_values = [min(pair) for pair in tree]
best_value = max(root_values)

print("EXPERIMENT 7 - Minimax Algorithm")
print("Values of MIN nodes:", root_values)
print("Best value for MAX:", best_value)
