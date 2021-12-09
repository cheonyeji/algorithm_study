INF = 999999999

graph_matrix = [[0, 7, 5], [7, 0, INF], [5, INF, 0]]

print(graph_matrix)

graph_list = [[] for _ in range(3)]
graph_list[0].append((1, 7))
graph_list[0].append((2, 5))

graph_list[1].append((0, 7))

graph_list[2].append((0, 5))

print(graph_list)
