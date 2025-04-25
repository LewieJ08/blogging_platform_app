from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    return render_template("index.html")

@app.route("/create", methods=["GET","POST"])

def create():
    return render_template("create.html")

@app.route("/update", methods=["GET","POST"])

def update():
    return render_template("update.html")

@app.route("/delete", methods=["GET","POST"])

def delete():
    return render_template("delete.html")

@app.route("/search", methods=["GET","POST"])

def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)