from time import perf_counter
from heapq import heappush, heappop
from collections import deque as queue

from helpers import calc_distance


def associations_to_path(associations: dict, goal_id: str, nodes) -> list:
    this_id = goal_id
    path = queue()
    while not this_id is None:
        path.appendleft(nodes[this_id])
        this_id = associations[this_id]
    return list(path)


def solve_dijkstra(start_id: str, end_id: str, nodes, edges):
    """
    Get the shortest distance between two nodes using Dijkstra's algorithm.

    :param start_id: ID of the start node
    :param end_id: ID of the end node
    :return: Shortest distance between start and end node
    """
    solution_t_start = perf_counter()

    solution = []
    associations = {start_id: None}

    visited = set()
    fringe = []

    start_y, start_x = nodes[start_id]
    start_node = (0, start_id)
    heappush(fringe, start_node)

    while True:
        c_node = heappop(fringe)
        c_distance, c_id = c_node
        c_y, c_x = nodes[c_id]

        if c_id not in visited:
            visited.add(c_id)
            if c_id == end_id:  # Solution found
                return c_distance, solution, perf_counter() - solution_t_start, associations_to_path(associations, c_id,
                                                                                                     nodes)
            else:
                for child_id, c_to_child_distance in edges[c_id]:
                    if child_id not in visited:
                        # Add to solution path
                        if child_id not in associations:
                            associations[child_id] = c_id

                        # Add child node to the fringe with the new cost
                        heappush(fringe, (c_distance + c_to_child_distance, child_id))
                        child_y, child_x = nodes[child_id]

                        solution.append(((c_y, c_x), (child_y, child_x)))


def solve_a_star(start_id: str, end_id: str, nodes, edges):
    """
    Get the shortest distance between two nodes using Dijkstra's algorithm.

    :param start_id: ID of the start node
    :param end_id: ID of the end node
    :return: Shortest distance between start and end node
    """
    solution_t_start = perf_counter()

    solution = []
    associations = {start_id: None}

    closed = set()  # Nodes that have been resolved
    fringe = []  # Min-heap that holds nodes to check (aka. fringe)

    start_y, start_x = nodes[start_id]
    end_y, end_x = nodes[end_id]

    start_node = (0 + calc_distance(start_y, start_x, end_y, end_x), 0, start_id)
    heappush(fringe, start_node)

    while len(fringe) > 0:
        c_node = heappop(fringe)
        c_f, c_distance, c_id = c_node
        c_y, c_x = nodes[c_id]
        if c_id == end_id:
            return c_distance, solution, perf_counter() - solution_t_start, associations_to_path(associations, c_id,
                                                                                                 nodes)
        if c_id not in closed:
            closed.add(c_id)
            for child_id, c_to_child_distance in edges[c_id]:
                if child_id not in closed:
                    # Add to solution path
                    if child_id not in associations:
                        associations[child_id] = c_id

                    child_distance = c_distance + c_to_child_distance  # Cost function
                    child_y, child_x = nodes[child_id]
                    child_node = (
                        child_distance + calc_distance(child_y, child_x, end_y, end_x), child_distance, child_id)
                    heappush(fringe, child_node)

                    solution.append(((c_y, c_x), (child_y, child_x)))
    return None
