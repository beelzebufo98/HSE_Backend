from flask import Flask, jsonify, request,render_template
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__, template_folder='../templates')


def get_port() -> int:
    config = dotenv_values(".env")
    return int(config.get("PORT", 5000))

@app.route("/author")
def author():
    author_info = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return jsonify(author_info)

@app.route("/author_info")
def author_in():
    author_info = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return render_template("author.html",author=author_info)


@app.route("/")
def server_info():
    server_info = "My Server!"
    return render_template("index.html", server_info=server_info)

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
