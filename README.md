
---

# 🩺 Diabetes Early Detection Web App (Flask + ML)

A **machine learning powered web application** that predicts the risk of diabetes based on user health parameters.
The project uses a **trained SVM model**, Flask for backend, and a modern HTML/CSS frontend for user interaction.

This tool is intended for **educational and early-risk awareness purposes only** and does not replace professional medical diagnosis.

---

## 🚀 Features

* 🔍 Predicts diabetes risk using Machine Learning (SVM)
* 🧠 Model trained on diabetes dataset
* 🌐 Web-based UI using Flask + HTML/CSS
* 📊 Data preprocessing with MinMax Scaling
* ⚡ Fast predictions with server-side inference
* ☁️ Deployment-ready (Vercel compatible)

---

## 🧰 Tech Stack

* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn (SVM)
* **Data Processing:** NumPy, Pandas
* **Frontend:** HTML5, CSS3
* **Model Serialization:** Pickle
* **Deployment:** Vercel (Serverless)

---

## 📂 Project Structure

```
project-root/
│
├── api/
│   └── app.py              # Flask backend (serverless compatible)
│
├── templates/
│   └── index.html          # Frontend UI
│
├── model.pkl               # Trained ML model
├── diabetes.csv            # Dataset used for scaling
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel configuration
└── README.md
```

---

## 🧠 Machine Learning Details

* **Algorithm:** Support Vector Machine (SVM)
* **Features Used:**

  * Glucose Level
  * Insulin Level
  * BMI
  * Age
* **Preprocessing:** MinMaxScaler (0–1 range)
* **Model Version Compatibility:**
  Trained using `scikit-learn==0.20.1`

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the application locally

```bash
python api/app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 How It Works

1. User enters health parameters via the web form
2. Input data is scaled using MinMaxScaler
3. Scaled values are passed to the trained SVM model
4. Model predicts diabetes risk (0 or 1)
5. Result is displayed dynamically on the UI

---

## ☁️ Deployment (Vercel)

* Flask app adapted to **serverless architecture**
* Uses `handler(event, context)` for Vercel execution
* Configured using `vercel.json`

### Deploy Steps (Summary)

1. Push code to GitHub
2. Import repository into Vercel
3. Select framework: **Other**
4. Deploy 🚀

---

## ⚠️ Disclaimer

⚕️ **Medical Disclaimer:**
This application is for educational and informational purposes only.
It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare provider for medical concerns.

---

## 📌 Future Improvements

* Convert backend to FastAPI
* Add REST API endpoints
* Retrain model with updated datasets
* Improve prediction explanations
* Add authentication and data logging

---

## 👨‍💻 Author

**Rahul Bhatia**
BTech in AI & ML
Passionate about Machine Learning, Web Development, and Data Science

---

