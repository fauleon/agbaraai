from flask import Flask, render_template, request


app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/lead")
def lead():
    data = {
        "name": request.form.get("name", "").strip(),
        "phone": request.form.get("phone", "").strip(),
        "goal": request.form.get("goal", "").strip(),
    }
    return render_template("index.html", lead_sent=True, lead=data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
