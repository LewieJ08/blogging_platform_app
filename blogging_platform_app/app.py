from flask import Flask, render_template, request, url_for, redirect
from database import init_database, create_post

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    return render_template("index.html")

@app.route("/create", methods=["GET","POST"])

def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        category = request.form["category"]
        tags = request.form["tags"]

        if not title or not content or not category:
            print("form field empty")
            return render_template("create.html", title = None)
        
        tags = tags.split(",")

        create_post(title,content,category,tags)
        return render_template("create.html", title = title)
    
    return render_template("create.html", title = None)

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
    init_database()
    app.run(debug=True)