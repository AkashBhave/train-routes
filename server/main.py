from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/solve", methods=["GET"])
def handle_solve():
    return "Solving..."

if __name__ == "__main__":
    app.run()