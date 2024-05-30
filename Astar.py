import heapq


def heuristic(graph, current, unvisited):
    if not unvisited:
        return 0
    return min(graph[current][city] for city in unvisited)


def a_star_tsp(graph, start):
    n = len(graph)
    pq = [(0, start, start, [start])]
    best_path, min_cost = None, float('inf')

    while pq:
        estimated_cost, cost, current, path = heapq.heappop(pq)
        unvisited = set(range(n)) - set(path)

        if len(path) == n:
            cost += graph[current][start]
            path.append(start)
            if cost < min_cost:
                best_path, min_cost = path, cost
            continue

        for neighbor in unvisited:
            new_cost = cost + graph[current][neighbor]
            estimated_cost = new_cost + heuristic(graph, neighbor, unvisited - {neighbor})
            heapq.heappush(pq, (estimated_cost, new_cost, neighbor, path + [neighbor]))

    return best_path, min_cost
