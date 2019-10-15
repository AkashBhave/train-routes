from collections import defaultdict

from helpers import calc_distance


def get_data(nodes_name: str, edges_name: str, names_name: str):
    nodes = {}
    edges = defaultdict(set)
    names = {}

    with open(f"data/{nodes_name}.txt", "r") as f_nodes:
        for f_node_line in f_nodes:
            node_id, node_lat, node_lon = f_node_line.strip().split(" ")
            nodes[node_id] = (node_lat, node_lon)

    with open(f"data/{edges_name}.txt", "r") as f_edges:
        for f_edges_line in f_edges:
            node1, node2 = f_edges_line.strip().split(" ")
            node1_coords, node2_coords = nodes[node1], nodes[node2]  # coords in the form (lat, lon)

            distance = calc_distance(node1_coords[0], node1_coords[1], node2_coords[0], node2_coords[1])
            edges[node1].add((node2, distance))
            edges[node2].add((node1, distance))

    with open(f"data/{names_name}.txt", "r") as f_names:
        for f_name in f_names:
            f_name = f_name.strip()
            node_id, node_name = f_name[:7], f_name[8:]
            names[node_name] = node_id

    return nodes, edges, names
