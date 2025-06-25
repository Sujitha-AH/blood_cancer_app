from flask import Flask, render_template, request
import pandas as pd
import joblib
import fitz  # PyMuPDF
import os

app = Flask(__name__)

# Load model and dataset
model = joblib.load("model.pkl")
df = pd.read_csv("medical_image_dataset_balanced.csv")
df['Target'] = df['Diagnosis'].apply(lambda x: 1 if x == "Leukemia" else 0)
feature_names = df.drop(columns=["Diagnosis", "Target"]).columns.tolist()

def extract_values_from_pdf(pdf_path, feature_names):
    extracted_data = {}
    doc = fitz.open(pdf_path)
    for page in doc:
        text = page.get_text()
        for line in text.split('\n'):
            for feature in feature_names:
                if feature.replace('_', ' ') in line:
                    try:
                        value = line.split(':')[-1].strip()
                        extracted_data[feature] = float(value)
                    except:
                        pass
    return extracted_data

@app.route("/")
def home():
    return render_template("index.html", features=feature_names)

@app.route("/predict", methods=["POST"])
def predict():
    extracted = {}

    # OPTION 1: PDF upload
    if 'pdf' in request.files and request.files['pdf'].filename != '':
        file = request.files['pdf']
        os.makedirs('uploads', exist_ok=True)
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        extracted = extract_values_from_pdf(filepath, feature_names)

    # OPTION 2: Manual entry
    else:
        for feature in feature_names:
            value = request.form.get(feature)
            if value:
                extracted[feature] = float(value)

    if len(extracted) != len(feature_names):
        missing = set(feature_names) - set(extracted.keys())
        return f"Missing data: {', '.join(missing)}", 400

    input_df = pd.DataFrame([extracted])
    prediction = model.predict(input_df)[0]
    result = "Leukemia (Blood Cancer)" if prediction == 1 else "No Blood Cancer"
    advice = "⚠️ Consult a hematologist. Start medication, hydrate, and monitor WBCs." if prediction == 1 else ""

    return render_template("result.html", result=result, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
