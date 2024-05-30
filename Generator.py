import random


def generate_random_graph(num_nodes, weight_range=(1, 20)):
    graph = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(*weight_range)
            graph[i][j] = weight
            graph[j][i] = weight
    print("Graph:")
    for row in graph:
        print(row)
    return graph
