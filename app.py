
from apps import create_app
from flask import redirect, url_for

app = create_app()

@app.route("/")
def index():
    return redirect(url_for("main.index"))


if __name__ == "__main__":
    app.run(debug=True)
