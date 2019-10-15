from flask import Flask

app = Flask(__name__)

from data import get_data


@app.route("/solve", methods=["GET"])
def handle_solve():
    return "Solving..."


if __name__ == "__main__":
    nodes, edges, names = get_data("nodes", "edges", "names")

    print(nodes)

    app.run()
