from flask import Flask, render_template
from newrelic_logs import configure_new_relic_logs


app = Flask(__name__)
configure_new_relic_logs("agbara")


@app.get("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
