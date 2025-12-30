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
#
#
#
#
#
# import os
# import pickle
# import streamlit as st
# from datetime import datetime
# from streamlit_option_menu import option_menu
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
#
# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Health Assistant",
#     page_icon="🧑‍⚕️",
#     layout="wide"
# )
#
# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>
# .big-card {
#     padding: 25px;
#     border-radius: 15px;
#     background-color: #0f172a;
#     box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
#     margin-bottom: 20px;
# }
# .result-positive {
#     color: #ff4b4b;
#     font-size: 22px;
#     font-weight: bold;
# }
# .result-negative {
#     color: #00ff9c;
#     font-size: 22px;
#     font-weight: bold;
# }
# </style>
# """, unsafe_allow_html=True)
#
# # ---------------- LOAD MODELS ----------------
# working_dir = os.path.dirname(os.path.abspath(__file__))
#
# diabetes_model = pickle.load(open(os.path.join(working_dir, "diabetes_model.sav"), "rb"))
# heart_disease_model = pickle.load(open(os.path.join(working_dir, "heart_disease_model.sav"), "rb"))
#
# # ---------------- PDF FUNCTION ----------------
# def generate_medical_pdf(
#     patient_name,
#     age,
#     gender,
#     disease_name,
#     inputs_dict,
#     result_text,
#     filename="medical_report.pdf"
# ):
#     styles = getSampleStyleSheet()
#     content = []
#
#     content.append(Paragraph("Medical Prediction Report", styles["Title"]))
#     content.append(Paragraph(
#         f"Date & Time: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
#         styles["Normal"]
#     ))
#
#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph("Patient Details", styles["Heading2"]))
#     content.append(Paragraph(f"Name: {patient_name}", styles["Normal"]))
#     content.append(Paragraph(f"Age: {age}", styles["Normal"]))
#     content.append(Paragraph(f"Gender: {gender}", styles["Normal"]))
#
#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph("Disease Tested", styles["Heading2"]))
#     content.append(Paragraph(disease_name, styles["Normal"]))
#
#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph("Medical Parameters", styles["Heading2"]))
#     for key, value in inputs_dict.items():
#         content.append(Paragraph(f"{key}: {value}", styles["Normal"]))
#
#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph("Prediction Result", styles["Heading2"]))
#     content.append(Paragraph(result_text, styles["Normal"]))
#
#     pdf = SimpleDocTemplate(filename)
#     pdf.build(content)
#
# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     selected = option_menu(
#         "Multiple Disease Prediction System",
#         ["Diabetes Prediction",
#          "Heart Disease Prediction",
#          "Project Info"],
#         icons=["activity", "heart", "info-circle"],
#         menu_icon="hospital-fill",
#         default_index=0
#     )
#
#     st.markdown("### 📊 Model Accuracy")
#     st.success("Diabetes Model: 78%")
#     st.success("Heart Disease Model: 82%")
#
# # ===================== DIABETES =====================
# if selected == "Diabetes Prediction":
#
#     st.markdown('<div class="big-card"><h2>🩸 Diabetes Prediction</h2></div>', unsafe_allow_html=True)
#
#     st.subheader("👤 Patient Details")
#     colp1, colp2, colp3 = st.columns(3)
#
#     with colp1:
#         patient_name = st.text_input("Patient Name")
#     with colp2:
#         patient_age = st.text_input("Age")
#     with colp3:
#         patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#
#     st.subheader("🧪 Medical Inputs")
#     col1, col2, col3 = st.columns(3)
#
#     with col1:
#         Pregnancies = st.text_input("Pregnancies")
#         SkinThickness = st.text_input("Skin Thickness")
#         DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
#
#     with col2:
#         Glucose = st.text_input("Glucose Level")
#         Insulin = st.text_input("Insulin Level")
#         Age = st.text_input("Patient Age")
#
#     with col3:
#         BloodPressure = st.text_input("Blood Pressure")
#         BMI = st.text_input("BMI")
#
#     if st.button("Diabetes Test Result"):
#         if patient_name == "" or patient_age == "":
#             st.warning("⚠️ Please enter patient details")
#         elif "" in [Pregnancies, Glucose, BloodPressure, SkinThickness,
#                     Insulin, BMI, DiabetesPedigreeFunction, Age]:
#             st.warning("⚠️ Please fill all medical fields")
#         else:
#             user_input = [
#                 float(Pregnancies), float(Glucose), float(BloodPressure),
#                 float(SkinThickness), float(Insulin), float(BMI),
#                 float(DiabetesPedigreeFunction), float(Age)
#             ]
#
#             result = diabetes_model.predict([user_input])
#
#             if result[0] == 1:
#                 msg = "The person is Diabetic"
#                 st.markdown(f'<p class="result-positive">{msg}</p>', unsafe_allow_html=True)
#             else:
#                 msg = "The person is NOT Diabetic"
#                 st.markdown(f'<p class="result-negative">{msg}</p>', unsafe_allow_html=True)
#
#             inputs_dict = {
#                 "Pregnancies": Pregnancies,
#                 "Glucose": Glucose,
#                 "Blood Pressure": BloodPressure,
#                 "Skin Thickness": SkinThickness,
#                 "Insulin": Insulin,
#                 "BMI": BMI,
#                 "Diabetes Pedigree Function": DiabetesPedigreeFunction
#             }
#
#             generate_medical_pdf(
#                 patient_name,
#                 patient_age,
#                 patient_gender,
#                 "Diabetes",
#                 inputs_dict,
#                 msg
#             )
#
#             with open("medical_report.pdf", "rb") as f:
#                 st.download_button(
#                     "📄 Download Detailed Medical Report",
#                     f,
#                     file_name=f"{patient_name}_diabetes_report.pdf"
#                 )
#
# # ===================== HEART =====================
# elif selected == "Heart Disease Prediction":
#
#     st.markdown('<div class="big-card"><h2>❤️ Heart Disease Prediction</h2></div>', unsafe_allow_html=True)
#
#     st.subheader("👤 Patient Details")
#     colp1, colp2, colp3 = st.columns(3)
#
#     with colp1:
#         patient_name = st.text_input("Patient Name")
#     with colp2:
#         patient_age = st.text_input("Age")
#     with colp3:
#         patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#
#     st.subheader("🧪 Medical Inputs")
#     col1, col2, col3 = st.columns(3)
#
#     with col1:
#         age = st.text_input("Age")
#         trestbps = st.text_input("Resting BP")
#         restecg = st.text_input("Rest ECG")
#         oldpeak = st.text_input("ST Depression")
#
#     with col2:
#         sex = st.text_input("Sex (0/1)")
#         chol = st.text_input("Cholesterol")
#         thalach = st.text_input("Max Heart Rate")
#         slope = st.text_input("Slope")
#
#     with col3:
#         cp = st.text_input("Chest Pain Type")
#         fbs = st.text_input("Fasting Blood Sugar")
#         exang = st.text_input("Exercise Induced Angina")
#         ca = st.text_input("Major Vessels")
#         thal = st.text_input("Thal")
#
#     if st.button("Heart Disease Test Result"):
#         if patient_name == "" or patient_age == "":
#             st.warning("⚠️ Please enter patient details")
#         elif "" in [age, sex, cp, trestbps, chol, fbs,
#                     restecg, thalach, exang, oldpeak,
#                     slope, ca, thal]:
#             st.warning("⚠️ Please fill all medical fields")
#         else:
#             user_input = [
#                 float(age), float(sex), float(cp), float(trestbps),
#                 float(chol), float(fbs), float(restecg), float(thalach),
#                 float(exang), float(oldpeak), float(slope),
#                 float(ca), float(thal)
#             ]
#
#             result = heart_disease_model.predict([user_input])
#
#             if result[0] == 1:
#                 msg = "The person HAS Heart Disease"
#                 st.markdown(f'<p class="result-positive">{msg}</p>', unsafe_allow_html=True)
#             else:
#                 msg = "The person does NOT have Heart Disease"
#                 st.markdown(f'<p class="result-negative">{msg}</p>', unsafe_allow_html=True)
#
#             inputs_dict = {
#                 "Age": age,
#                 "Sex": sex,
#                 "Chest Pain": cp,
#                 "Resting BP": trestbps,
#                 "Cholesterol": chol,
#                 "Fasting Blood Sugar": fbs,
#                 "Rest ECG": restecg,
#                 "Max Heart Rate": thalach,
#                 "Exercise Angina": exang,
#                 "ST Depression": oldpeak,
#                 "Slope": slope,
#                 "Major Vessels": ca,
#                 "Thal": thal
#             }
#
#             generate_medical_pdf(
#                 patient_name,
#                 patient_age,
#                 patient_gender,
#                 "Heart Disease",
#                 inputs_dict,
#                 msg
#             )
#
#             with open("medical_report.pdf", "rb") as f:
#                 st.download_button(
#                     "📄 Download Detailed Medical Report",
#                     f,
#                     file_name=f"{patient_name}_heart_report.pdf"
#                 )
#
# # ===================== PROJECT INFO =====================
# elif selected == "Project Info":
#     st.title("📘 Project Information")
#     st.markdown("""
#     **Multiple Disease Prediction System**
#
#     - Streamlit-based ML health assistant
#     - Predicts Diabetes and Heart Disease
#     - Generates detailed medical PDF reports
#     - Includes patient details and test parameters
#     - Developed as a Final Year Project
#     """)


import os
import pickle
import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu

# PDF + QR
import qrcode
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import lightgrey

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Health Assistant", layout="wide")

# ---------------- LOAD MODELS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(os.path.join(BASE_DIR, "diabetes_model.sav"), "rb"))
heart_disease_model = pickle.load(open(os.path.join(BASE_DIR, "heart_disease_model.sav"), "rb"))

# ---------------- PDF FUNCTION ----------------
def generate_medical_pdf(name, age, gender, disease, params, result, filename="medical_report.pdf"):
    styles = getSampleStyleSheet()
    content = []

    qr_text = f"""
    Patient: {name}
    Age: {age}
    Gender: {gender}
    Disease: {disease}
    Result: {result}
    Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}
    """

    qr = qrcode.make(qr_text)
    qr.save("qr.png")

    content.append(Paragraph("Medical Prediction Report", styles["Title"]))
    content.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}", styles["Normal"]))
    content.append(Paragraph("<br/>", styles["Normal"]))

    content.append(Paragraph("<b>Patient Details</b>", styles["Heading2"]))
    content.append(Paragraph(f"Name: {name}", styles["Normal"]))
    content.append(Paragraph(f"Age: {age}", styles["Normal"]))
    content.append(Paragraph(f"Gender: {gender}", styles["Normal"]))

    content.append(Paragraph("<br/>", styles["Normal"]))
    content.append(Paragraph(f"<b>Disease:</b> {disease}", styles["Normal"]))

    content.append(Paragraph("<br/>", styles["Normal"]))
    content.append(Paragraph("<b>Medical Parameters</b>", styles["Heading2"]))
    for k, v in params.items():
        content.append(Paragraph(f"{k}: {v}", styles["Normal"]))

    content.append(Paragraph("<br/>", styles["Normal"]))
    content.append(Paragraph(f"<b>Result:</b> {result}", styles["Normal"]))
    content.append(Image("qr.png", width=120, height=120))

    pdf = SimpleDocTemplate(filename, pagesize=A4)

    def watermark(c, d):
        c.saveState()
        c.setFont("Helvetica-Bold", 40)
        c.setFillColor(lightgrey)
        c.translate(300, 400)
        c.rotate(45)
        c.drawCentredString(0, 0, "Rahul Nayak")
        c.restoreState()

    pdf.build(content, onFirstPage=watermark, onLaterPages=watermark)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        "Disease Prediction",
        ["Diabetes Prediction", "Heart Disease Prediction"],
        icons=["activity", "heart"],
        menu_icon="hospital-fill"
    )

# ===================== DIABETES =====================
if selected == "Diabetes Prediction":
    st.title("🩸 Diabetes Prediction")

    st.subheader("Patient Details")
    patient_name = st.text_input("Patient Name", key="d_name")
    patient_age = st.text_input("Patient Age", key="d_page")
    patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="d_gender")

    st.subheader("Medical Inputs")
    Pregnancies = st.text_input("Pregnancies", key="d_preg")
    Glucose = st.text_input("Glucose", key="d_glu")
    BP = st.text_input("Blood Pressure", key="d_bp")
    Skin = st.text_input("Skin Thickness", key="d_skin")
    Insulin = st.text_input("Insulin", key="d_ins")
    BMI = st.text_input("BMI", key="d_bmi")
    DPF = st.text_input("Diabetes Pedigree Function", key="d_dpf")
    Age = st.text_input("Age (Medical)", key="d_age")

    if st.button("Predict Diabetes"):
        data = [Pregnancies, Glucose, BP, Skin, Insulin, BMI, DPF, Age]
        if "" in data or patient_name == "":
            st.warning("Fill all fields")
        else:
            data = list(map(float, data))
            result = diabetes_model.predict([data])
            msg = "Diabetic" if result[0] == 1 else "Not Diabetic"
            st.success(msg)

            generate_medical_pdf(
                patient_name, patient_age, patient_gender,
                "Diabetes", {
                    "Pregnancies": Pregnancies,
                    "Glucose": Glucose,
                    "BP": BP,
                    "BMI": BMI
                }, msg
            )

            with open("medical_report.pdf", "rb") as f:
                st.download_button("Download Report", f, file_name="diabetes_report.pdf")

# ===================== HEART =====================
elif selected == "Heart Disease Prediction":
    st.title("❤️ Heart Disease Prediction")

    st.subheader("Patient Details")
    patient_name = st.text_input("Patient Name", key="h_name")
    patient_age = st.text_input("Patient Age", key="h_page")
    patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="h_gender")

    st.subheader("Medical Inputs")
    age = st.text_input("Age", key="h_age")
    sex = st.text_input("Sex (0/1)", key="h_sex")
    cp = st.text_input("Chest Pain", key="h_cp")
    trestbps = st.text_input("Resting BP", key="h_bp")
    chol = st.text_input("Cholesterol", key="h_chol")
    fbs = st.text_input("FBS", key="h_fbs")
    restecg = st.text_input("Rest ECG", key="h_ecg")
    thalach = st.text_input("Max HR", key="h_hr")
    exang = st.text_input("Exercise Angina", key="h_ex")
    oldpeak = st.text_input("Oldpeak", key="h_old")
    slope = st.text_input("Slope", key="h_slope")
    ca = st.text_input("CA", key="h_ca")
    thal = st.text_input("Thal", key="h_thal")

    if st.button("Predict Heart Disease"):
        data = [age, sex, cp, trestbps, chol, fbs, restecg,
                thalach, exang, oldpeak, slope, ca, thal]

        if "" in data or patient_name == "":
            st.warning("Fill all fields")
        else:
            data = list(map(float, data))
            result = heart_disease_model.predict([data])
            msg = "Heart Disease Detected" if result[0] == 1 else "No Heart Disease"
            st.success(msg)

            generate_medical_pdf(
                patient_name, patient_age, patient_gender,
                "Heart Disease", {
                    "Age": age,
                    "Cholesterol": chol,
                    "BP": trestbps
                }, msg
            )

            with open("medical_report.pdf", "rb") as f:
                st.download_button("Download Report", f, file_name="heart_report.pdf")