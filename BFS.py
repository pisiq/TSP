from collections import deque


def bfs_tsp(graph, start):
    n = len(graph)
    queue = deque([(start, [start], 0)])
    best_path, min_cost = None, float('inf')

    while queue:
        current, path, cost = queue.popleft()

        if len(path) == n:

            cost += graph[current][start]
            path.append(start)
            if cost < min_cost:
                best_path, min_cost = path, cost
            continue

        for neighbor in range(n):
            if neighbor not in path:
                new_cost = cost + graph[current][neighbor]
                queue.append((neighbor, path + [neighbor], new_cost))

    return best_path, min_cost
