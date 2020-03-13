from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_profs/<title>')
def index(title):
    params = dict()
    params["title"] = title
    return render_template("list_profs.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
