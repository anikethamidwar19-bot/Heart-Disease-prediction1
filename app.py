from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained Binary Classification model
with open("KNN_project (1).pkl", "rb") as f:
    model = pickle.load(f)


# Encoding dictionaries
gender_map = {
    "Male": 1,
    "Female": 0
}

binary_map = {
    "No": 0,
    "Yes": 1
}

ordinal_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get numerical inputs
        age = float(request.form["age"])
        blood_pressure = float(request.form["blood_pressure"])
        cholesterol_level = float(request.form["cholesterol_level"])
        bmi = float(request.form["bmi"])
        sleep_hours = float(request.form["sleep_hours"])
        triglyceride_level = float(request.form["triglyceride_level"])
        fasting_blood_sugar = float(request.form["fasting_blood_sugar"])
        crp_level = float(request.form["crp_level"])
        homocysteine_level = float(request.form["homocysteine_level"])

        # Get categorical inputs and encode them
        gender = gender_map[request.form["gender"]]

        exercise_habits = ordinal_map[request.form["exercise_habits"]]

        smoking = binary_map[request.form["smoking"]]

        family_heart_disease = binary_map[
            request.form["family_heart_disease"]
        ]

        diabetes = binary_map[request.form["diabetes"]]

        high_blood_pressure = binary_map[
            request.form["high_blood_pressure"]
        ]

        low_hdl_cholesterol = binary_map[
            request.form["low_hdl_cholesterol"]
        ]

        high_ldl_cholesterol = binary_map[
            request.form["high_ldl_cholesterol"]
        ]

        alcohol_consumption = ordinal_map[
            request.form["alcohol_consumption"]
        ]

        stress_level = ordinal_map[
            request.form["stress_level"]
        ]

        sugar_consumption = ordinal_map[
            request.form["sugar_consumption"]
        ]

        # Arrange all 20 features in dataset order
        features = [
            age,
            gender,
            blood_pressure,
            cholesterol_level,
            exercise_habits,
            smoking,
            family_heart_disease,
            diabetes,
            bmi,
            high_blood_pressure,
            low_hdl_cholesterol,
            high_ldl_cholesterol,
            alcohol_consumption,
            stress_level,
            sleep_hours,
            sugar_consumption,
            triglyceride_level,
            fasting_blood_sugar,
            crp_level,
            homocysteine_level
        ]

        # Convert features into a 2D NumPy array
        final_features = np.array([features])

        # Make binary classification prediction
        prediction = model.predict(final_features)[0]

        # Convert prediction into Yes or No
        if prediction in [1, "1", "Yes"]:
            output = "Heart Disease: Yes"
        else:
            output = "Heart Disease: No"

        return render_template(
            "index.html",
            prediction_text=output
        )

    except Exception as e:

        print("Prediction Error:", e)

        return render_template(
            "index.html",
            prediction_text="Error in prediction. Check your inputs and model."
        )


if __name__ == "__main__":
    app.run(debug=True)