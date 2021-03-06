from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return "Hello, World"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello there {name+ '12' } with years old {age+1}!"


@app.route("/html")
def dance():
    return '<h1>Hello, world</h1>'\
            '<img src="https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02' \
           '/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1"/> '


if __name__ == "__main__":
    app.run(debug=True)
