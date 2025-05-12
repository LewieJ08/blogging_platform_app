from flask import Flask, render_template, request, jsonify
from database import init_database, search_posts, create_post, update_post, delete_post, get_all_posts, get_post_by_id

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    posts = get_all_posts()

    if posts == []:
        return render_template("index.html", posts = None)
    
    return render_template("index.html", posts = posts)

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

@app.route("/update", methods=["GET","POST","PUT"])

def update():
    posts = get_all_posts()

    if posts == []:
        return render_template("update.html", title = None, posts = None)

    if request.method == "POST":
        return render_template("update.html", title = False)
    
    elif request.method == "PUT":
        data = request.get_json()
        post_id = request.args.get("post_id")

        if not data["title"] or not data["content"] or not data["category"]:
            print("form field empty")
            return render_template("update.html", title = False)
        
        title = data["title"]
        content = data["content"]
        category = data["category"]
        tags = data["tags"]

        tags = tags.split(",")

        update_post(title,content,category,tags,post_id)
        
        return jsonify({"message": "post updated successfully"}, 200)

    return render_template("update.html", posts = posts, title = None)

@app.route("/delete", methods=["GET","POST","DELETE"])

def delete():
    posts = get_all_posts()

    if posts == []:
        return render_template("delete.html", posts = None)

    elif request.method == "DELETE":
        post_id = request.args.get("post_id")
        delete_post(post_id)

    return render_template("delete.html", posts = posts)

@app.route("/search", methods=["GET","POST"])

def search():
    posts = get_all_posts()
    if request.method == "POST":
        term = request.form["term"]

        posts = search_posts(term)

        if posts == []:
            return render_template("search.html", posts = False)

        return render_template("search.html", posts = posts)

    return render_template("search.html", posts = posts)

@app.route("/post/<int:post_id>", methods=["GET","POST"])

def post(post_id):
    post = get_post_by_id(post_id)
    formatted_post = post[0]

    raw_tags = formatted_post[4]
    tags = raw_tags.strip("{}").split(",")

    return render_template("post.html", post = formatted_post, tags = tags)

if __name__ == "__main__":
    init_database()
    app.run(debug=True)