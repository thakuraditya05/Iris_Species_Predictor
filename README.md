# 🌸 Iris Species Predictor
**A Professional Machine Learning Dashboard for Botanical Classification**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)

## 📖 Project Overview
The **Iris Species Predictor** is an interactive web application designed to classify Iris flowers into three species: **Setosa, Versicolor, and Virginica**. By leveraging a Random Forest Machine Learning model, the app analyzes leaf structures—specifically the length and width of sepals and petals—to provide instant, accurate predictions.

  <img width="1919" height="873" alt="Screenshot 2026-01-05 122034" src="https://github.com/user-attachments/assets/7724d596-3219-4736-a78b-8e69ee500785" />


---

## ✨ Key Features
* **Personalized User Experience:** A custom greeting form that remembers your name throughout the session.
* **Dynamic UI Toggling:** Utilizing `st.session_state`, the app intelligently switches between the input form and the results dashboard to reduce screen clutter.
* **Data Exploration:** An expandable section providing a "unique look" at the dataset with example rows for each class.
* **Real-time Analysis:** High-visibility metrics and visual animations (balloons!) upon successful prediction.
* **Responsive Design:** Optimized column layouts for a clean, dashboard-style feel.

---

## 🛠️ Technology Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (Random Forest Classifier)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)

---

## 🚀 How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/iris-species-predictor.git
    cd iris-species-predictor
    ```

2.  **Install Requirements**
    Make sure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the App**
    ```bash
    streamlit run iris_prediction.py
    ```

---


## 📂 Project Structure
* To run the project locally, maintain the following directory structure:
  ```text
  ├── iris_prediction.py     # Main Streamlit application code
  ├── requirements.txt      # List of dependencies for deployment
  └── README.md             # Project documentation (this file)

--- 



## 🔍 Feature Definitions & 📊 Dataset Information

* The model is trained on the Fisher's Iris Dataset, which consists of 150 samples from three species of Iris and The model analyzes four specific physical dimensions of the Iris flower to determine its species:
  
  | Feature | Type | Description |
  | :--- | :--- | :--- |
  | **Sepal Length** | Numeric (cm) | The length of the outer, typically green, protective leaves. |
  | **Sepal Width** | Numeric (cm) | The maximum width of the outer green leaves. |
  | **Petal Length** | Numeric (cm) | The length of the inner, colorful, pollinator-attracting petals. |
  | **Petal Width** | Numeric (cm) | The maximum width of the inner colorful petals. |

---
## 👤 Author

Aditya Singh
* **GitHub:** [thakuraditya05](https://github.com/thakuraditya05) & [thakur-aditya05](https://github.com/thakur-aditya05) 
* **LinkedIn:** [thakuraditya05](https://www.linkedin.com/in/thakuraditya05/)

--- 
