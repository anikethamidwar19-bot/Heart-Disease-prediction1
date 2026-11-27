# 💚 Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

The **Heart Disease Prediction System** is a Machine Learning-based web application developed using Python and Flask. It predicts the possibility of heart disease based on various health parameters, lifestyle habits, and medical history.

The project uses a trained Binary Classification model to classify the prediction into two categories:

- **Yes** – Heart disease predicted.
- **No** – Heart disease not predicted.

The application provides a user-friendly interface with a modern Black & Neon Green theme.

## 🚀 Technologies Used

- **Python** – Programming language
- **Machine Learning** – Binary Classification
- **Scikit-learn** – Machine Learning library
- **Flask** – Web application framework
- **NumPy** – Numerical operations
- **HTML5** – Web page structure
- **CSS3** – Website styling
- **Pickle** – Saving and loading the trained ML model

## 📊 Input Features

The application uses 20 input features:

| Category | Features |
|---|---|
| Personal Information | Age, Gender |
| Health Measurements | Blood Pressure, Cholesterol Level, BMI, Sleep Hours |
| Medical Parameters | Triglyceride Level, Fasting Blood Sugar, CRP Level, Homocysteine Level |
| Lifestyle | Exercise Habits, Smoking, Alcohol Consumption, Stress Level, Sugar Consumption |
| Medical History | Family Heart Disease, Diabetes, High Blood Pressure, Low HDL Cholesterol, High LDL Cholesterol |

## ⚙️ Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── Binary_Classification.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## 🔧 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to Project Folder

```bash
cd Heart-Disease-Prediction
```

### Step 3: Install Required Libraries

```bash
pip install flask numpy scikit-learn
```

### Step 4: Run the Flask Application

```bash
python app.py
```

### Step 5: Open in Browser

```text
http://127.0.0.1:5000/
```

## 🖥️ Application Features

- User-friendly input form.
- 20 health-related input parameters.
- Categorical data encoding.
- Machine Learning-based binary classification.
- Real-time prediction through Flask.
- Responsive web interface.
- Black & Neon Green user interface.

## 🧠 Machine Learning Workflow

1. Collect health-related input data.
2. Preprocess numerical and categorical features.
3. Encode categorical variables into numerical values.
4. Train a Binary Classification model.
5. Save the trained model using Pickle.
6. Load the trained model into Flask.
7. Accept user inputs through the web application.
8. Generate predictions using the trained model.

## 📷 Project Screenshots

Add your application screenshots here after uploading them to your GitHub repository.

Example:

```markdown
![Home Page](screenshots/homepage.png)

![Prediction Result](screenshots/prediction.png)
```

## 🎯 Project Objective

The main objective of this project is to understand how Machine Learning classification algorithms can be integrated into a web application to process health-related information and generate predictions.

## 👨‍💻 Author

**Aniketh Amidwar**

B.Tech – Information Technology

Interested in Data Science, Machine Learning, Artificial Intelligence, and Data Analytics.

## ⚠️ Disclaimer

This project is developed for educational and learning purposes only. The predictions are not medically validated and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---

⭐ If you find this project useful, consider giving this repository a star!
