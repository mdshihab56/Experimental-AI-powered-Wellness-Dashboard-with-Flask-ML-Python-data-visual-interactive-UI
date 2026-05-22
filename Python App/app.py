from flask import Flask, render_template
from flask import request, jsonify
from model import predict_status
import matplotlib.pyplot as plt
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    sleep = int(data["sleep"])
    stress = int(data["stress"])
    productivity = int(data["productivity"])
    water = int(data["water"])
    screen = int(data["screen"])
    exercise = int(data["exercise"])
    moodText = data["moodText"]
    result = predict_status(
        sleep,
        stress,
        productivity,
        water,
        screen,
        exercise,
        moodText
    )
    plt.clf()
    plt.figure(figsize=(8,4))
    values = [
        sleep,
        stress,
        productivity,
        water,
        screen,
        exercise
    ]
    labels = [
        "Sleep",
        "Stress",
        "Productivity",
        "Water",
        "Screen",
        "Exercise"
    ]
    plt.plot(
        labels,
        values,
        marker="o",
        linewidth=3
    )
    ideal = [8, 2, 8, 8, 3, 30]
    plt.plot(
        labels,
        ideal,
        linestyle="--"
    )
    plt.title("AI Wellness Analytics")
    plt.grid(True)
    plt.savefig("static/chart.png")
    return jsonify({
        "result": result
    })
if __name__ == "__main__":

    app.run(debug=True)