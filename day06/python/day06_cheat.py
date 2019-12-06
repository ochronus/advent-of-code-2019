import networkx as nx


with open('../input.txt', 'r') as file:
    data = [l.strip().split(')') for l in file.readlines()]
graph = nx.Graph(data)
print(sum(nx.shortest_path_length(graph, space_object, "COM") for space_object in graph.nodes)) 
print(nx.shortest_path_length(graph, "YOU", "SAN") - 2)     # let's not count the start and the end
