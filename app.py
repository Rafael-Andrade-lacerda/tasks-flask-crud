from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "aaaa"


@app.route("/about")
def about():
    return "Bom dia mae"


if __name__ == "__main__":
    app.run(debug=True)
