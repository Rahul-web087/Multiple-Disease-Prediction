# # import os
# # import pickle
# # import streamlit as st
# # import numpy as np
# # from streamlit_option_menu import option_menu
# # from reportlab.platypus import SimpleDocTemplate, Paragraph
# # from reportlab.lib.styles import getSampleStyleSheet
# #
# # # ---------------- PAGE CONFIG ----------------
# # st.set_page_config(
# #     page_title="Health Assistant",
# #     page_icon="🧑‍⚕️",
# #     layout="wide"
# # )
# #
# # # ---------------- CUSTOM CSS ----------------
# # st.markdown("""
# # <style>
# # .big-card {
# #     padding: 25px;
# #     border-radius: 15px;
# #     background-color: #0f172a;
# #     box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
# #     margin-bottom: 20px;
# # }
# # .result-positive {
# #     color: #ff4b4b;
# #     font-size: 22px;
# #     font-weight: bold;
# # }
# # .result-negative {
# #     color: #00ff9c;
# #     font-size: 22px;
# #     font-weight: bold;
# # }
# # </style>
# # """, unsafe_allow_html=True)
# #
# # # ---------------- LOAD MODELS ----------------
# # working_dir = os.path.dirname(os.path.abspath(__file__))
# #
# # diabetes_model = pickle.load(open(os.path.join(working_dir, "diabetes_model.sav"), "rb"))
# # heart_disease_model = pickle.load(open(os.path.join(working_dir, "heart_disease_model.sav"), "rb"))
# # parkinsons_model = pickle.load(open(os.path.join(working_dir, "parkinsons_model.sav"), "rb"))
# #
# # # ---------------- PDF FUNCTION ----------------
# # def generate_pdf(text, filename="medical_report.pdf"):
# #     pdf = SimpleDocTemplate(filename)
# #     styles = getSampleStyleSheet()
# #     content = [
# #         Paragraph("Medical Prediction Report", styles["Title"]),
# #         Paragraph(text, styles["Normal"])
# #     ]
# #     pdf.build(content)
# #
# # # ---------------- SIDEBAR ----------------
# # with st.sidebar:
# #     selected = option_menu(
# #         "Multiple Disease Prediction System",
# #         ["Diabetes Prediction",
# #          "Heart Disease Prediction",
# #          "Parkinson Disease Prediction",
# #          "Project Info"],
# #         icons=["activity", "heart", "person", "info-circle"],
# #         menu_icon="hospital-fill",
# #         default_index=0
# #     )
# #
# #     st.markdown("### 📊 Model Accuracy")
# #     st.success("Diabetes Model: 78%")
# #     st.success("Heart Disease Model: 82%")
# #     st.success("Parkinson Model: 87%")
# #
# # # ===================== DIABETES =====================
# # if selected == "Diabetes Prediction":
# #
# #     st.markdown('<div class="big-card"><h2>🩸 Diabetes Prediction</h2></div>', unsafe_allow_html=True)
# #
# #     col1, col2, col3 = st.columns(3)
# #
# #     with col1:
# #         Pregnancies = st.text_input("Number of Pregnancies")
# #         SkinThickness = st.text_input("Skin Thickness")
# #         DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
# #
# #     with col2:
# #         Glucose = st.text_input("Glucose Level")
# #         Insulin = st.text_input("Insulin Level")
# #         Age = st.text_input("Age")
# #
# #     with col3:
# #         BloodPressure = st.text_input("Blood Pressure")
# #         BMI = st.text_input("BMI")
# #
# #     if st.button("Diabetes Test Result"):
# #         user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness,
# #                       Insulin, BMI, DiabetesPedigreeFunction, Age]
# #
# #         if "" in user_input:
# #             st.warning("⚠️ Please fill all fields")
# #         else:
# #             user_input = [float(x) for x in user_input]
# #             result = diabetes_model.predict([user_input])
# #
# #             if result[0] == 1:
# #                 msg = "The person is Diabetic"
# #                 st.markdown(f'<p class="result-positive">{msg}</p>', unsafe_allow_html=True)
# #             else:
# #                 msg = "The person is NOT Diabetic"
# #                 st.markdown(f'<p class="result-negative">{msg}</p>', unsafe_allow_html=True)
# #
# #             generate_pdf(msg)
# #             with open("medical_report.pdf", "rb") as f:
# #                 st.download_button("📄 Download Medical Report", f, "medical_report.pdf")
# #
# # # ===================== HEART =====================
# # elif selected == "Heart Disease Prediction":
# #
# #     st.markdown('<div class="big-card"><h2>❤️ Heart Disease Prediction</h2></div>', unsafe_allow_html=True)
# #
# #     col1, col2, col3 = st.columns(3)
# #
# #     with col1:
# #         age = st.text_input("Age")
# #         trestbps = st.text_input("Resting BP")
# #         restecg = st.text_input("Rest ECG")
# #         oldpeak = st.text_input("ST Depression")
# #
# #     with col2:
# #         sex = st.text_input("Sex")
# #         chol = st.text_input("Cholesterol")
# #         thalach = st.text_input("Max Heart Rate")
# #         slope = st.text_input("Slope")
# #
# #     with col3:
# #         cp = st.text_input("Chest Pain Type")
# #         fbs = st.text_input("Fasting Blood Sugar")
# #         exang = st.text_input("Exercise Induced Angina")
# #         ca = st.text_input("Major Vessels")
# #         thal = st.text_input("Thal")
# #
# #     if st.button("Heart Disease Test Result"):
# #         user_input = [age, sex, cp, trestbps, chol, fbs,
# #                       restecg, thalach, exang, oldpeak,
# #                       slope, ca, thal]
# #
# #         if "" in user_input:
# #             st.warning("⚠️ Please fill all fields")
# #         else:
# #             user_input = [float(x) for x in user_input]
# #             result = heart_disease_model.predict([user_input])
# #
# #             if result[0] == 1:
# #                 msg = "The person HAS Heart Disease"
# #                 st.markdown(f'<p class="result-positive">{msg}</p>', unsafe_allow_html=True)
# #             else:
# #                 msg = "The person does NOT have Heart Disease"
# #                 st.markdown(f'<p class="result-negative">{msg}</p>', unsafe_allow_html=True)
# #
# #             generate_pdf(msg)
# #             with open("medical_report.pdf", "rb") as f:
# #                 st.download_button("📄 Download Medical Report", f, "medical_report.pdf")
# #
# # # ===================== PARKINSON =====================
# # elif selected == "Parkinson Disease Prediction":
# #
# #     st.markdown('<div class="big-card"><h2>🧠 Parkinson Disease Prediction</h2></div>', unsafe_allow_html=True)
# #
# #     col1, col2, col3 = st.columns(3)
# #
# #     with col1:
# #         fo = st.text_input("MDVP:Fo")
# #         RAP = st.text_input("RAP")
# #         HNR = st.text_input("HNR")
# #
# #     with col2:
# #         fhi = st.text_input("MDVP:Fhi")
# #         PPQ = st.text_input("PPQ")
# #         RPDE = st.text_input("RPDE")
# #
# #     with col3:
# #         flo = st.text_input("MDVP:Flo")
# #         DDP = st.text_input("DDP")
# #         DFA = st.text_input("DFA")
# #
# #     if st.button("Parkinson's Test Result"):
# #         user_input = [fo, fhi, flo, RAP, PPQ, DDP, HNR, RPDE, DFA]
# #
# #         if "" in user_input:
# #             st.warning("⚠️ Please fill all fields")
# #         else:
# #             user_input = [float(x) for x in user_input]
# #             result = parkinsons_model.predict([user_input])
# #
# #             if result[0] == 1:
# #                 msg = "The person HAS Parkinson's Disease"
# #                 st.markdown(f'<p class="result-positive">{msg}</p>', unsafe_allow_html=True)
# #             else:
# #                 msg = "The person does NOT have Parkinson's Disease"
# #                 st.markdown(f'<p class="result-negative">{msg}</p>', unsafe_allow_html=True)
# #
# #             generate_pdf(msg)
# #             with open("medical_report.pdf", "rb") as f:
# #                 st.download_button("📄 Download Medical Report", f, "medical_report.pdf")
# #
# # # ===================== PROJECT INFO =====================
# # elif selected == "Project Info":
# #     st.title("📘 Project Information")
# #
# #     st.markdown("""
# #     **Multiple Disease Prediction System**
# #
# #     - Built using **Streamlit**
# #     - Machine Learning Models (Logistic Regression / SVM)
# #     - Diseases Covered:
# #         - Diabetes
# #         - Heart Disease
# #         - Parkinson’s Disease
# #     - Features:
# #         - User-friendly UI
# #         - PDF Medical Report
# #         - Model Accuracy Display
# #     - Developed as a **Final Year Project**
# #     """)
#






import pickle
import streamlit as st
import numpy as np
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import qrcode

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="Health Assistant",
    page_icon="🧑‍⚕️",
    layout="wide"
)

st.title("🧑‍⚕️ Multiple Disease Prediction System")

# ===============================
# Load Models
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(os.path.join(BASE_DIR, "diabetes_model.sav"), "rb"))
heart_model = pickle.load(open(os.path.join(BASE_DIR, "heart_disease_model.sav"), "rb"))

# ===============================
# Doctor Advice Logic
# ===============================
def get_doctor_advice(disease, prediction):
    if disease == "Diabetes":
        return (
            "• Consult a physician.\n"
            "• Maintain a low-sugar diet.\n"
            "• Exercise regularly.\n"
            "• Monitor blood glucose."
            if prediction == 1 else
            "• Maintain healthy lifestyle.\n"
            "• Balanced diet & exercise.\n"
            "• Regular checkups advised."
        )

    if disease == "Heart Disease":
        return (
            "• Consult a cardiologist immediately.\n"
            "• Avoid smoking & alcohol.\n"
            "• Heart-healthy diet.\n"
            "• Take medicines regularly."
            if prediction == 1 else
            "• Healthy diet & exercise.\n"
            "• Stress management.\n"
            "• Routine heart checkups."
        )

# ===============================
# PDF Generator (with QR Code)
# ===============================
def generate_pdf(patient_name, age, gender, disease, result, advice):
    file_name = f"{patient_name.replace(' ', '_')}_Medical_Report.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # ---------- QR CODE ----------
    app_url = "https://multiple-disease-prediction.onrender.com"
    qr_img = qrcode.make(app_url)
    qr_path = "qr_temp.png"
    qr_img.save(qr_path)

    # ---------- TITLE ----------
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, "Medical Prediction Report")

    # ---------- CONTENT ----------
    c.setFont("Helvetica", 12)
    y = height - 120

    c.drawString(50, y, f"Patient Name: {patient_name}"); y -= 25
    c.drawString(50, y, f"Age: {age}"); y -= 25
    c.drawString(50, y, f"Gender: {gender}"); y -= 25
    c.drawString(50, y, f"Disease Checked: {disease}"); y -= 25
    c.drawString(50, y, f"Prediction Result: {result}"); y -= 35

    # ---------- DOCTOR ADVICE ----------
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Doctor's Advice:"); y -= 25
    c.setFont("Helvetica", 12)

    for line in advice.split("\n"):
        c.drawString(70, y, line)
        y -= 18

    # ---------- DATE ----------
    y -= 10
    c.drawString(
        50, y,
        f"Date & Time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    # ---------- QR ----------
    c.drawImage(qr_path, width - 170, 80, width=100, height=100)
    c.drawString(width - 170, 65, "Scan to open App")

    # ---------- WATERMARK ----------
    c.setFont("Helvetica-Bold", 40)
    c.setFillGray(0.9, 0.4)
    c.drawCentredString(width / 2, height / 2, "Rahul Nayak")

    c.save()

    if os.path.exists(qr_path):
        os.remove(qr_path)

    return file_name

# ===============================
# Sidebar Menu
# ===============================
menu = st.sidebar.selectbox(
    "Select Prediction",
    ["Diabetes Prediction", "Heart Disease Prediction"]
)

# ===============================
# Patient Details (COMMON)
# ===============================
st.subheader("👤 Patient Details")

patient_name = st.text_input("Patient Name", key="patient_name")
patient_age = st.number_input("Patient Age", 1, 120, 35, key="patient_age")
gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="patient_gender")

# ======================================================
# 🩸 DIABETES
# ======================================================
if menu == "Diabetes Prediction":

    st.header("🩸 Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input("Pregnancies", 0, key="dia_preg")
        glucose = st.number_input("Glucose Level", 0, key="dia_glucose")
        bp = st.number_input("Blood Pressure", 0, key="dia_bp")

    with col2:
        skin = st.number_input("Skin Thickness", 0, key="dia_skin")
        insulin = st.number_input("Insulin Level", 0, key="dia_insulin")
        bmi = st.number_input("BMI", 0.0, key="dia_bmi")

    with col3:
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, key="dia_dpf")

    if st.button("Predict Diabetes"):
        if patient_name == "":
            st.warning("Please enter patient name")
        else:
            input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, patient_age]])
            prediction = diabetes_model.predict(input_data)[0]

            result = "Diabetes Detected ❌" if prediction == 1 else "No Diabetes ✅"
            st.success(result)

            advice = get_doctor_advice("Diabetes", prediction)
            pdf = generate_pdf(patient_name, patient_age, gender, "Diabetes", result, advice)

            with open(pdf, "rb") as f:
                st.download_button("📄 Download Medical Report", f, file_name=pdf)

# ======================================================
# ❤️ HEART DISEASE
# ======================================================
if menu == "Heart Disease Prediction":

    st.header("❤️ Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.selectbox("Sex (Male=1, Female=0)", ["Male", "Female"], key="heart_sex")
        cp = st.number_input("Chest Pain Type (0-3)", 0, 3, key="heart_cp")

    with col2:
        trestbps = st.number_input("Resting BP", 50, key="heart_trestbps")
        chol = st.number_input("Cholesterol", 100, key="heart_chol")
        fbs = st.number_input("Fasting Blood Sugar (0/1)", 0, 1, key="heart_fbs")

    with col3:
        restecg = st.number_input("Rest ECG (0-2)", 0, 2, key="heart_restecg")
        thalach = st.number_input("Max Heart Rate", 60, key="heart_thalach")
        exang = st.number_input("Exercise Angina (0/1)", 0, 1, key="heart_exang")

    col4, col5, col6 = st.columns(3)
    with col4:
        oldpeak = st.number_input("Oldpeak", 0.0, key="heart_oldpeak")
    with col5:
        slope = st.number_input("Slope (0-2)", 0, 2, key="heart_slope")
    with col6:
        ca = st.number_input("CA (0-4)", 0, 4, key="heart_ca")

    thal = st.number_input("Thal (0=normal,1=fixed,2=reversible)", 0, 2, key="heart_thal")

    if st.button("Predict Heart Disease"):
        if patient_name == "":
            st.warning("Please enter patient name")
        else:
            sex_val = 1 if sex == "Male" else 0

            input_data = np.array([[
                patient_age, sex_val, cp, trestbps, chol,
                fbs, restecg, thalach, exang,
                oldpeak, slope, ca, thal
            ]])

            prediction = heart_model.predict(input_data)[0]

            result = "Heart Disease Detected ❌" if prediction == 1 else "No Heart Disease ✅"
            st.success(result)

            advice = get_doctor_advice("Heart Disease", prediction)
            pdf = generate_pdf(patient_name, patient_age, gender, "Heart Disease", result, advice)

            with open(pdf, "rb") as f:
                st.download_button("📄 Download Medical Report", f, file_name=pdf)

# ===============================
# Footer
# ===============================
st.markdown("---")
st.caption("© Developed by Rahul Nayak ")

