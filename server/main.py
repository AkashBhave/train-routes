from flask import Flask, request, jsonify

app = Flask(__name__)

from data import get_data
from algorithms import *


@app.route("/solve", methods=["GET"])
def handle_solve():
    algorithms = {"dijk": solve_dijkstra, "a": solve_a_star}

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
    return str(algorithm(names[user_city1], names[user_city2], nodes, edges))


if __name__ == "__main__":
    nodes, edges, names = get_data("nodes", "edges", "names")

    app.run()
