from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", tempo=datetime.datetime.utcnow())

if __name__ == "__main__":
    app.run(port=6000)