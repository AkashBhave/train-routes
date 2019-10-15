from flask import Flask, request, jsonify

app = Flask(__name__)

from data import get_data
from algorithms import *


@app.route("/solve", methods=["GET"])
def handle_solve():
    algorithms = {"dijkstra": solve_dijkstra, "a": solve_a_star}

    user_algorithm = request.args.get("algorithm")
    user_city1 = request.args.get("city1")
    user_city2 = request.args.get("city2")

    # Check the arguments
    if user_algorithm is None or user_algorithm not in algorithms:
        return "Invalid algorithm name"
    if user_city1 is None or user_city1.strip() not in names:
        return "Invalid city (1) name"
    if user_city2 is None or user_city2.strip() not in names:
        return "Invalid city (2) name"

    algorithm = algorithms[user_algorithm]

    s = algorithm(names[user_city1], names[user_city2], nodes, edges)

    if s is None:
        return "Error in computations"

    s_dist, s_path, s_runtime = s

    return jsonify({
        "distance": s_dist,
        "runtime": s_runtime,
        "solution": s_path
    })


if __name__ == "__main__":
    nodes, edges, names = get_data("nodes", "edges", "names")

    app.run()
