from time import perf_counter
from heapq import heappush, heappop
from collections import deque as queue
from itertools import count

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


def solve_bfs(start_id: str, end_id: str, nodes, edges):
    solution_t_start = perf_counter()

    solution = []

    # Initialize data structures
    fringe = queue()  # Queue to hold nodes to check since it's FIFO
    visited = {}  # Dict/hash-map for nodes already checked: key = node, value = parent

    # Add initial node to collections
    fringe.append((0, start_id))
    visited[start_id] = None  # Start node has no parents

    while len(fringe) > 0:
        current_distance, current_id = fringe.popleft()
        current_y, current_x = nodes[current_id]
        if current_id == end_id:
            this_id = current_id
            path = queue()
            while not this_id == start_id:
                path.appendleft(this_id)
                this_id = visited[this_id]
            return current_distance, solution, perf_counter() - solution_t_start, associations_to_path(visited, end_id,
                                                                                                       nodes)
        for child_id, c_to_child_distance in edges[current_id]:
            if child_id not in visited:
                fringe.append((current_distance + c_to_child_distance, child_id))
                visited[child_id] = current_id

                child_y, child_x = nodes[child_id]
                solution.append(((current_y, current_x), (child_y, child_x)))

    return None


def solve_id_dfs(start_id: str, end_id: str, nodes, edges):
    solution_t_start = perf_counter()

    solution_all = []

    def k_dfs(s_id: str, k: int):
        fringe = []  # Stack to hold nodes to check

        start_node = (s_id, 0, {s_id}, [])  # (string representation, depth, ancestors)
        fringe.append(start_node)

        while len(fringe) > 0:  # Keep iterating until the fringe is empty
            c_node = fringe.pop()
            c_id, c_distance, c_ancestors, c_path = c_node
            c_y, c_x = nodes[c_id]
            c_children = edges[c_id]
            if c_id == end_id:
                return c_node
            if c_distance < k:
                for child_id, c_to_child_distance in c_children:
                    if child_id not in c_ancestors:
                        child_node = (child_id,
                                      c_distance + c_to_child_distance,
                                      c_ancestors.union({child_id}),
                                      [*c_path, child_id])
                        fringe.append(child_node)

                        child_y, child_x = nodes[child_id]
                        if ((c_y, c_x), (child_y, child_x)) not in solution_all:
                            solution_all.append(((c_y, c_x), (child_y, child_x)))
        return None

    for depth in count():
        solution = k_dfs(start_id, depth * 100)
        print(depth * 100)
        if solution is not None and solution[0] == end_id:
            solution_path = [nodes[n] for n in solution[3]]
            return solution[1], solution_all, perf_counter() - solution_t_start, solution_path


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
