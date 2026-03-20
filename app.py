from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form.get("news")

        if not data:
            return render_template("index.html", prediction="No input given")

        vec = vectorizer.transform([data])
        result = model.predict(vec)

        prediction = "Real News" if result[0] == 1 else "Fake News"

        return render_template("index.html", prediction=prediction)

    except Exception as e:
        return str(e)   # 🔥 will show real error

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)