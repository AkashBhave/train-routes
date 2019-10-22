from data import get_data
from algorithms import *

from flask import Flask, request, jsonify, Response
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/solve", methods=["GET"])
@cross_origin()
def handle_solve():
    algorithms = {"dijkstra": solve_dijkstra, "a": solve_a_star, "bfs": solve_bfs, "iddfs": solve_id_dfs}

    user_algorithm = request.args.get("algorithm")
    user_city1 = request.args.get("city1")
    user_city2 = request.args.get("city2")

    # Check the arguments
    if user_algorithm is None or user_algorithm not in algorithms:
        return "Invalid algorithm name", 400
    if user_city1 is None or user_city1.strip() not in names:
        return "Invalid city (1) name", 400
    if user_city2 is None or user_city2.strip() not in names:
        return "Invalid city (2) name", 400

    try:
        algorithm = algorithms[user_algorithm]

        s = algorithm(names[user_city1], names[user_city2], nodes, edges)

        if s is None:
            return "Error in computations", 500

        s_dist, s_all, s_runtime, s_path = s

        return jsonify({
            "distance": s_dist,
            "runtime": s_runtime,
            "solution": s_all,
            "path": s_path
        }), 200
    except ValueError:
        return "Error in computations", 500


if __name__ == "__main__":
    nodes, edges, names = get_data("nodes", "edges", "names")

    app.run()
