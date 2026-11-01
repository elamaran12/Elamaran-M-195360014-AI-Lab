# EXPERIMENT 8: Implementing Alpha-Beta Pruning

# Binary game tree with 8 leaf scores.
tree = [
    [3, 5],
    [6, 9],
    [1, 2],
    [0, -1]
]
visited_leaves = 0
pruned_leaves = 0

def alphabeta(node, depth, alpha, beta, maximizing):
    global visited_leaves, pruned_leaves

    if depth == 2:
        visited_leaves += 1
        return node

    if maximizing:
        value = float("-inf")
        for i, child in enumerate(node):
            value = max(value, alphabeta(child, depth + 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                # Count leaf scores skipped in remaining branches.
                pruned_leaves += sum_leaf_count(node[i + 1:])
                break
        return value
    else:
        value = float("inf")
        for i, child in enumerate(node):
            value = min(value, alphabeta(child, depth + 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                pruned_leaves += sum_leaf_count(node[i + 1:])
                break
        return value

def sum_leaf_count(nodes):
    count = 0
    for item in nodes:
        if isinstance(item, list):
            count += sum_leaf_count(item)
        else:
            count += 1
    return count

# Root MAX, level 1 MIN, level 2 MAX, leaves are numeric.
value = alphabeta(tree, 0, float("-inf"), float("inf"), True)

print("EXPERIMENT 8 - Alpha-Beta Pruning")
print("Best value for MAX:", value)
print("Leaf nodes evaluated:", visited_leaves)
print("Leaf values pruned:", pruned_leaves)
