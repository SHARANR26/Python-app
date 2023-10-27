from flask import Flask

app = Flask(_name_)  # noqa: F821

@app.route("/")
def hello():
    return "Hellow Sharan !"