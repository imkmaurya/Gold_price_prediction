# 🪙 Gold Price Prediction App

## 📌 Overview

This project predicts gold prices using Machine Learning techniques.
It uses historical financial data and applies regression models to estimate future gold prices.

---

## 🚀 Features

* 📊 Data preprocessing (handling missing values, scaling, encoding)
* 🤖 Model training using XGBoost
* 📈 Evaluation using R² score
* 🌐 Interactive web app using Streamlit
* ⚡ Real-time prediction with user input

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Streamlit

---

## 📂 Project Structure

```
├── app.py                 # Streamlit app
├── model_pipeline.pkl     # Trained ML pipeline
├── requirements.txt       # Dependencies
├── notebook.ipynb         # Model training
```

---

## ⚙️ How it Works

1. Data is preprocessed using scaling and encoding
2. A machine learning model is trained
3. The model is saved using joblib
4. Streamlit app takes user input
5. Input is processed and prediction is displayed

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

This app is deployed using Streamlit Community Cloud.

---

## 📊 Model Performance

* Train R² Score: **0.87**
* Test R² Score: **0.82**

---

## 🧠 Key Learnings

* Importance of data preprocessing
* Handling categorical variables
* Model deployment with Streamlit
* Using pipelines for consistent predictions

---

## 🙌 Author

Your Name

---
