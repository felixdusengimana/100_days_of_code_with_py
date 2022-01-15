from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello there {name+ '12' } with years old {age+1}!"


if __name__ == "__main__":
    app.run(debug=True)
