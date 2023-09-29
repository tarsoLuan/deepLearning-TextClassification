from flask import Flask, render_template, request, jsonify
from chat import get_response
import pandas as pd

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    json_ = request.json
    print(json_)
    response = get_response(json_['message'])

    message = {"answer": response}

    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)