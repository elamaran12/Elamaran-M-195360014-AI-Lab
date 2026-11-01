from collections import deque

# EXPERIMENT 3: State-Space Search for Water Resource Allocation
def water_jug(cap1, cap2, target):
    queue = deque([((0, 0), [(0, 0)])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        if a == target or b == target:
            return path

        pour_a_to_b = min(a, cap2 - b)
        pour_b_to_a = min(b, cap1 - a)

        next_states = [
            (cap1, b), (a, cap2), (0, b), (a, 0),
            (a - pour_a_to_b, b + pour_a_to_b),
            (a + pour_b_to_a, b - pour_b_to_a)
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))

    return None

result = water_jug(4, 3, 2)
print("EXPERIMENT 3 - State-Space Search for Water Resource Allocation")
if result:
    print("Steps (4-litre jug, 3-litre jug):")
    for state in result:
        print(state)
else:
    print("Target cannot be reached")
