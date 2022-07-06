from flask import Flask, render_template, request, url_for, redirect

from back import get_items, get_images

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f"<h1> Hello </h1>"



@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        tag = request.form["searchbar"]
        return redirect(url_for("galerie", tags=tag))
    else:
        return render_template("formulaire.html")

@app.route("/<tags>")
def galerie(tags):
    tag = tags
    if request.method == "GET":
        paths = get_items(tag)
        print(paths)
        list_images = get_images(paths)
        print (list_images)
        return render_template("galerie.html", list_images=list_images)

    #return f"<h1> {paths} </h1>"
    return redirect(url_for("galerie", tags=tag))

app.route("")
if __name__ == '__main__':
    app.run()
