import heapq


def lc_tsp(graph, start):
    n = len(graph)
    pq = [(0, start, [start])]
    best_path, min_cost = None, float('inf')

    while pq:
        cost, current, path = heapq.heappop(pq)

        if len(path) == n:
            cost += graph[current][start]
            path.append(start)
            if cost < min_cost:
                best_path, min_cost = path, cost
            continue

        for neighbor in range(n):
            if neighbor not in path:
                new_cost = cost + graph[current][neighbor]
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return best_path, min_cost
