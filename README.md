# 🩸 Blood Cancer Prediction Web App

A Flask-based machine learning web application that predicts **Leukemia (Blood Cancer)** using blood report data. Users can either **upload a PDF report** or **manually enter values** to check the diagnosis.

---

## 🚀 Features

✅ Upload blood report as PDF and extract values automatically
✅ Manual form to enter values directly
✅ Predicts whether Leukemia (Blood Cancer) is detected or not
✅ Shows additional advice if cancer is detected
✅ Beautiful UI with center-aligned, colorful layout

---

## 🧪 Tech Stack

* **Frontend**: HTML, CSS (with inline styles)
* **Backend**: Flask (Python)
* **ML Model**: Trained with Scikit-learn, saved with Joblib
* **PDF Extraction**: PyMuPDF (fitz)
* **Data Handling**: Pandas

---

## 📝 How to Use

### 🌐 Option 1: Run Locally

1. Clone the repo:

```bash
git clone https://github.com/Sujitha-AH/blood_cancer_app.git
cd blood_cancer_app
```

2. Create virtual environment and activate:

```bash
python -m venv venv
venv\Scripts\activate  # for Windows
```

3. Install requirements:

```bash
pip install -r requirements.txt  # if requirements.txt is available
```

Or manually install:

```bash
pip install flask pandas joblib PyMuPDF scikit-learn
```

4. Run the app:

```bash
python app.py
```

5. Open browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📄 Sample PDFs

Two sample PDFs are included for demo:

* `sample_leukemia_report.pdf`
* `sample_normal_report.pdf`

You can upload these to test the prediction system.

---

## 💡 Expected PDF Format

The app extracts values from PDF in the format like:

```
WBC Count: 28000
RBC Count: 3800000
Hemoglobin: 9.5
... and so on
```

Make sure all features exist in the PDF with clear labels.

---

## ❤️ Author

**Sujitha AH** – Engineering student, dreamer, creator 💫
Crafted with love, learning, and brilliance 🥰

---

## 🌍 Live Deployment (Optional)

Want to make it live on the web? You can deploy using:

* Render
* PythonAnywhere
* Heroku

Message me if you want step-by-step help with that too 😉

---

## 📌 License

Open-source project for learning and showcasing 💡

---

Made with 💖 by [Sujitha AH](https://github.com/Sujitha-AH)
