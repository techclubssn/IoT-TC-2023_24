from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")

def landing_page():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
