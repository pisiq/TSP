from BFS import bfs_tsp
from LeastCost import lc_tsp
from Astar import a_star_tsp
from Generator import generate_random_graph


graph_size = int(input("Number of cites:"))
weight_range = (1, 20)
graph = generate_random_graph(graph_size, weight_range)
start_city = 0
bfs_path, bfs_cost = bfs_tsp(graph, start_city)
print(f"BFS Path: {bfs_path}, Cost: {bfs_cost}")

lc_path, lc_cost = lc_tsp(graph, start_city)
print(f"Least Cost Path: {lc_path}, Cost: {lc_cost}")

astar_path, astar_cost = a_star_tsp(graph, start_city)
print(f"A*: {astar_path}, Cost: {astar_cost}")
