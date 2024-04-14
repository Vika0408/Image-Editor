from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        return "POST request is here"
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
