from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)
GENDERLIZE_API_ENDPOINT = "https://api.genderize.io/"
AGEFY_API_ENDPOINT = "https://api.agify.io"


@app.route("/")
def home():
    random_number = random.randint(0, 100)
    return render_template("index.html", rand=random_number, year=datetime.now().year)


@app.route("/guess/<string:name>")
def guess(name):
    response = requests.get(url=GENDERLIZE_API_ENDPOINT, params={
        "name": name
    })
    response.raise_for_status()
    data = response.json()

    response2 = requests.get(url=AGEFY_API_ENDPOINT, params={
        "name": name
    })

    data2 = response2.json()

    return render_template("guess.html", name=data["name"], age=data2["age"], gender=data["gender"])


@app.route("/blog")
def blog():
    blog_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(blog_url)
    response.raise_for_status()
    return render_template("blog.html", all_blogs=response.json())


@app.route("/blog/<int:index>")
def show_post(index):
    blog_url = f"https://jsonplaceholder.typicode.com/posts/{index}"
    response = requests.get(blog_url)
    blog = response.json()

    user_url = f'https://jsonplaceholder.typicode.com/users/{blog["userId"]}'

    response2 = requests.get(user_url)
    user = response2.json()
    return render_template("singleblog.html", blog=blog,link_user=user["website"], creator=user["name"])


if __name__ == "__main__":
    app.run(debug=True)
