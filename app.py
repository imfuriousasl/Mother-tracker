from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

mothers = []

@app.route("/")
def index():
    today = datetime.today()

    display = []
    for m in mothers:
        days_since = (today - m["start_date"]).days
        total = m["base_days"] + days_since

        display.append({
            "name": m["name"],
            "total_days": total
        })

    return render_template("index.html", mothers=display)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    mode = request.form["mode"]

    today = datetime.today()

    if mode == "new":
        mothers.append({
            "name": name,
            "start_date": today,
            "base_days": 0
        })

    else:
        base = int(request.form["days"])
        mothers.append({
            "name": name,
            "start_date": today,
            "base_days": base
        })

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)