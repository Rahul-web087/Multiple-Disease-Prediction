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


# import os
# import pickle
# import streamlit as st
# from datetime import datetime
# from streamlit_option_menu import option_menu

# # PDF + QR
# import qrcode
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.colors import lightgrey

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Health Assistant", layout="wide")

# # ---------------- LOAD MODELS ----------------
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# diabetes_model = pickle.load(open(os.path.join(BASE_DIR, "diabetes_model.sav"), "rb"))
# heart_disease_model = pickle.load(open(os.path.join(BASE_DIR, "heart_disease_model.sav"), "rb"))

# # ---------------- PDF FUNCTION ----------------
# def generate_medical_pdf(name, age, gender, disease, params, result, filename="medical_report.pdf"):
#     styles = getSampleStyleSheet()
#     content = []

#     qr_text = f"""
#     Patient: {name}
#     Age: {age}
#     Gender: {gender}
#     Disease: {disease}
#     Result: {result}
#     Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}
#     """

#     qr = qrcode.make(qr_text)
#     qr.save("qr.png")

#     content.append(Paragraph("Medical Prediction Report", styles["Title"]))
#     content.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}", styles["Normal"]))
#     content.append(Paragraph("<br/>", styles["Normal"]))

#     content.append(Paragraph("<b>Patient Details</b>", styles["Heading2"]))
#     content.append(Paragraph(f"Name: {name}", styles["Normal"]))
#     content.append(Paragraph(f"Age: {age}", styles["Normal"]))
#     content.append(Paragraph(f"Gender: {gender}", styles["Normal"]))

#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph(f"<b>Disease:</b> {disease}", styles["Normal"]))

#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph("<b>Medical Parameters</b>", styles["Heading2"]))
#     for k, v in params.items():
#         content.append(Paragraph(f"{k}: {v}", styles["Normal"]))

#     content.append(Paragraph("<br/>", styles["Normal"]))
#     content.append(Paragraph(f"<b>Result:</b> {result}", styles["Normal"]))
#     content.append(Image("qr.png", width=120, height=120))

#     pdf = SimpleDocTemplate(filename, pagesize=A4)

#     def watermark(c, d):
#         c.saveState()
#         c.setFont("Helvetica-Bold", 40)
#         c.setFillColor(lightgrey)
#         c.translate(300, 400)
#         c.rotate(45)
#         c.drawCentredString(0, 0, "Rahul Nayak")
#         c.restoreState()

#     pdf.build(content, onFirstPage=watermark, onLaterPages=watermark)

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     selected = option_menu(
#         "Disease Prediction",
#         ["Diabetes Prediction", "Heart Disease Prediction"],
#         icons=["activity", "heart"],
#         menu_icon="hospital-fill"
#     )

# # ===================== DIABETES =====================
# if selected == "Diabetes Prediction":
#     st.title("🩸 Diabetes Prediction")

#     st.subheader("Patient Details")
#     patient_name = st.text_input("Patient Name", key="d_name")
#     patient_age = st.text_input("Patient Age", key="d_page")
#     patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="d_gender")

#     st.subheader("Medical Inputs")
#     Pregnancies = st.text_input("Pregnancies", key="d_preg")
#     Glucose = st.text_input("Glucose", key="d_glu")
#     BP = st.text_input("Blood Pressure", key="d_bp")
#     Skin = st.text_input("Skin Thickness", key="d_skin")
#     Insulin = st.text_input("Insulin", key="d_ins")
#     BMI = st.text_input("BMI", key="d_bmi")
#     DPF = st.text_input("Diabetes Pedigree Function", key="d_dpf")
#     Age = st.text_input("Age (Medical)", key="d_age")

#     if st.button("Predict Diabetes"):
#         data = [Pregnancies, Glucose, BP, Skin, Insulin, BMI, DPF, Age]
#         if "" in data or patient_name == "":
#             st.warning("Fill all fields")
#         else:
#             data = list(map(float, data))
#             result = diabetes_model.predict([data])
#             msg = "Diabetic" if result[0] == 1 else "Not Diabetic"
#             st.success(msg)

#             generate_medical_pdf(
#                 patient_name, patient_age, patient_gender,
#                 "Diabetes", {
#                     "Pregnancies": Pregnancies,
#                     "Glucose": Glucose,
#                     "BP": BP,
#                     "BMI": BMI
#                 }, msg
#             )

#             with open("medical_report.pdf", "rb") as f:
#                 st.download_button("Download Report", f, file_name="diabetes_report.pdf")

# # ===================== HEART =====================
# elif selected == "Heart Disease Prediction":
#     st.title("❤️ Heart Disease Prediction")

#     st.subheader("Patient Details")
#     patient_name = st.text_input("Patient Name", key="h_name")
#     patient_age = st.text_input("Patient Age", key="h_page")
#     patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="h_gender")

#     st.subheader("Medical Inputs")
#     age = st.text_input("Age", key="h_age")
#     sex = st.text_input("Sex (0/1)", key="h_sex")
#     cp = st.text_input("Chest Pain", key="h_cp")
#     trestbps = st.text_input("Resting BP", key="h_bp")
#     chol = st.text_input("Cholesterol", key="h_chol")
#     fbs = st.text_input("FBS", key="h_fbs")
#     restecg = st.text_input("Rest ECG", key="h_ecg")
#     thalach = st.text_input("Max HR", key="h_hr")
#     exang = st.text_input("Exercise Angina", key="h_ex")
#     oldpeak = st.text_input("Oldpeak", key="h_old")
#     slope = st.text_input("Slope", key="h_slope")
#     ca = st.text_input("CA", key="h_ca")
#     thal = st.text_input("Thal", key="h_thal")

#     if st.button("Predict Heart Disease"):
#         data = [age, sex, cp, trestbps, chol, fbs, restecg,
#                 thalach, exang, oldpeak, slope, ca, thal]

#         if "" in data or patient_name == "":
#             st.warning("Fill all fields")
#         else:
#             data = list(map(float, data))
#             result = heart_disease_model.predict([data])
#             msg = "Heart Disease Detected" if result[0] == 1 else "No Heart Disease"
#             st.success(msg)

#             generate_medical_pdf(
#                 patient_name, patient_age, patient_gender,
#                 "Heart Disease", {
#                     "Age": age,
#                     "Cholesterol": chol,
#                     "BP": trestbps
#                 }, msg
#             )

#             # with open("medical_report.pdf", "rb") as f:

#                 st.download_button("Download Report", f, file_name="heart_report.pdf")












# import pickle
# import streamlit as st
# import numpy as np
# import os

# # ===============================
# # Page Configuration
# # ===============================
# st.set_page_config(
#     page_title="Health Assistant",
#     page_icon="🧑‍⚕️",
#     layout="wide"
# )

# st.title("🧑‍⚕️ Multiple Disease Prediction System")

# # ===============================
# # Load Models
# # ===============================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# diabetes_model = pickle.load(open(os.path.join(BASE_DIR, "diabetes_model.sav"), "rb"))
# heart_model = pickle.load(open(os.path.join(BASE_DIR, "heart_disease_model.sav"), "rb"))

# # ===============================
# # Sidebar Menu
# # ===============================
# menu = st.sidebar.selectbox(
#     "Select Prediction",
#     ["Diabetes Prediction", "Heart Disease Prediction"]
# )

# # ======================================================
# # 🩸 DIABETES PREDICTION
# # ======================================================
# if menu == "Diabetes Prediction":

#     st.header("🩸 Diabetes Prediction")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         pregnancies = st.number_input("Pregnancies", min_value=0, value=0)
#         glucose = st.number_input("Glucose Level", min_value=0, value=120)
#         bp = st.number_input("Blood Pressure", min_value=0, value=70)

#     with col2:
#         skin = st.number_input("Skin Thickness", min_value=0, value=20)
#         insulin = st.number_input("Insulin Level", min_value=0, value=80)
#         bmi = st.number_input("BMI", min_value=0.0, value=25.0)

#     with col3:
#         dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5)
#         age = st.number_input("Age", min_value=1, value=30)

#     if st.button("Predict Diabetes"):
#         input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
#         prediction = diabetes_model.predict(input_data)

#         if prediction[0] == 1:
#             st.error("❌ Person is Diabetic")
#         else:
#             st.success("✅ Person is NOT Diabetic")

# # ======================================================
# # ❤️ HEART DISEASE PREDICTION
# # ======================================================
# if menu == "Heart Disease Prediction":

#     st.header("❤️ Heart Disease Prediction")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         age = st.number_input("Age", min_value=1, value=45)
#         sex = st.selectbox("Sex", ["Male", "Female"])
#         cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)

#     with col2:
#         trestbps = st.number_input("Resting Blood Pressure", min_value=50, value=120)
#         chol = st.number_input("Cholesterol", min_value=100, value=200)
#         fbs = st.number_input("Fasting Blood Sugar (0/1)", min_value=0, max_value=1)

#     with col3:
#         restecg = st.number_input("Rest ECG (0-2)", min_value=0, max_value=2)
#         thalach = st.number_input("Max Heart Rate", min_value=60, value=150)
#         exang = st.number_input("Exercise Angina (0/1)", min_value=0, max_value=1)

#     col4, col5, col6 = st.columns(3)

#     with col4:
#         oldpeak = st.number_input("Oldpeak", min_value=0.0, value=1.0)
#     with col5:
#         slope = st.number_input("Slope (0-2)", min_value=0, max_value=2)
#     with col6:
#         ca = st.number_input("CA (0-4)", min_value=0, max_value=4)

#     thal = st.number_input("Thal (0=normal,1=fixed,2=reversible)", min_value=0, max_value=2)

#     if st.button("Predict Heart Disease"):
#         sex_val = 1 if sex == "Male" else 0

#         input_data = np.array([[
#             age, sex_val, cp, trestbps, chol,
#             fbs, restecg, thalach, exang,
#             oldpeak, slope, ca, thal
#         ]])

#         prediction = heart_model.predict(input_data)

#         if prediction[0] == 1:
#             st.error("❌ Heart Disease Detected")
#         else:
#             st.success("✅ No Heart Disease Detected")

# # ===============================
# # Footer
# # ===============================
# st.markdown("---")
# st.caption("© Developed by Rahul Nayak | Deployed with Docker & Render")








import pickle
import streamlit as st
import numpy as np
import os
from datetime import datetime

# PDF & QR
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Health Assistant",
    page_icon="🧑‍⚕️",
    layout="wide"
)

# ===============================
# MODERN UI (CSS)
# ===============================
st.markdown("""
<style>
.main { background-color: #0f172a; }
h1, h2, h3 { color: #facc15; }
.stButton>button {
    background-color: #facc15;
    color: black;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧑‍⚕️ Multiple Disease Prediction System")

# ===============================
# LOAD MODELS (Cloud Safe)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(
    open(os.path.join(BASE_DIR, "diabetes_model.sav"), "rb")
)

heart_model = pickle.load(
    open(os.path.join(BASE_DIR, "heart_disease_model.sav"), "rb")
)

# ===============================
# PDF GENERATOR (Watermark + QR)
# ===============================
def generate_pdf(patient_name, age, gender, disease, result):
    file_name = "medical_report.pdf"

    # QR Code (Live App URL)
    app_url = "https://multiple-disease-prediction.onrender.com"
    qr = qrcode.make(app_url)
    qr_path = "qr_code.png"
    qr.save(qr_path)

    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Watermark
    c.setFont("Helvetica", 40)
    c.setFillGray(0.9)
    c.saveState()
    c.translate(300, 400)
    c.rotate(45)
    c.drawCentredString(0, 0, "Rahul Nayak")
    c.restoreState()

    # Title
    c.setFillGray(0)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "Medical Prediction Report")

    # Content
    c.setFont("Helvetica", 12)
    y = height - 100

    details = [
        f"Patient Name: {patient_name}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Disease Type: {disease}",
        f"Prediction Result: {result}",
        f"Date & Time: {datetime.now().strftime('%d-%m-%Y %H:%M')}"
    ]

    for line in details:
        c.drawString(50, y, line)
        y -= 30

    # QR Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, "Scan QR Code to Open Live Application:")
    c.drawImage(qr_path, 50, y - 180, width=120, height=120)

    c.save()
    return file_name

# ===============================
# SIDEBAR MENU
# ===============================
menu = st.sidebar.selectbox(
    "Select Prediction",
    ["Diabetes Prediction", "Heart Disease Prediction"]
)

# ======================================================
# 🩸 DIABETES PREDICTION
# ======================================================
if menu == "Diabetes Prediction":

    st.header("🩸 Diabetes Prediction")

    st.subheader("👤 Patient Details")
    p1, p2, p3 = st.columns(3)
    patient_name = p1.text_input("Patient Name")
    patient_age = p2.number_input("Age", min_value=1, value=30)
    patient_gender = p3.selectbox(
        "Gender", ["Male", "Female", "Other"]
    )

    st.subheader("🧪 Medical Inputs")
    c1, c2, c3 = st.columns(3)

    with c1:
        pregnancies = st.number_input("Pregnancies", min_value=0, value=0)
        glucose = st.number_input("Glucose Level", min_value=0, value=120)
        bp = st.number_input("Blood Pressure", min_value=0, value=70)

    with c2:
        skin = st.number_input("Skin Thickness", min_value=0, value=20)
        insulin = st.number_input("Insulin Level", min_value=0, value=80)
        bmi = st.number_input("BMI", min_value=0.0, value=25.0)

    with c3:
        dpf = st.number_input(
            "Diabetes Pedigree Function", min_value=0.0, value=0.5
        )
        age = st.number_input(
            "Age (Medical)", min_value=1, value=30
        )

    if st.button("Predict Diabetes"):
        if patient_name.strip() == "":
            st.warning("Please enter Patient Name")
        else:
            input_data = np.array([[
                pregnancies, glucose, bp, skin,
                insulin, bmi, dpf, age
            ]])

            prediction = diabetes_model.predict(input_data)

            if prediction[0] == 1:
                result_text = "POSITIVE (Diabetic)"
                st.error("❌ Person is Diabetic")
            else:
                result_text = "NEGATIVE (Not Diabetic)"
                st.success("✅ Person is NOT Diabetic")

            pdf_file = generate_pdf(
                patient_name,
                patient_age,
                patient_gender,
                "Diabetes",
                result_text
            )

            with open(pdf_file, "rb") as f:
                st.download_button(
                    "⬇️ Download Medical Report (PDF)",
                    f,
                    file_name="diabetes_medical_report.pdf",
                    mime="application/pdf"
                )

# ======================================================
# ❤️ HEART DISEASE PREDICTION
# ======================================================
if menu == "Heart Disease Prediction":

    st.header("❤️ Heart Disease Prediction")

    st.subheader("👤 Patient Details")
    p1, p2, p3 = st.columns(3)
    patient_name = p1.text_input("Patient Name")
    patient_age = p2.number_input("Age", min_value=1, value=45)
    patient_gender = p3.selectbox(
        "Gender", ["Male", "Female", "Other"]
    )

    st.subheader("🧪 Medical Inputs")
    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input("Age", min_value=1, value=45)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.number_input("Chest Pain Type (0–3)", min_value=0, max_value=3)

    with c2:
        trestbps = st.number_input("Resting BP", min_value=50, value=120)
        chol = st.number_input("Cholesterol", min_value=100, value=200)
        fbs = st.number_input(
            "Fasting Blood Sugar (0/1)", min_value=0, max_value=1
        )

    with c3:
        restecg = st.number_input(
            "Rest ECG (0–2)", min_value=0, max_value=2
        )
        thalach = st.number_input(
            "Max Heart Rate", min_value=60, value=150
        )
        exang = st.number_input(
            "Exercise Angina (0/1)", min_value=0, max_value=1
        )

    c4, c5, c6 = st.columns(3)
    with c4:
        oldpeak = st.number_input("Oldpeak", min_value=0.0, value=1.0)
    with c5:
        slope = st.number_input(
            "Slope (0–2)", min_value=0, max_value=2
        )
    with c6:
        ca = st.number_input(
            "CA (0–4)", min_value=0, max_value=4
        )

    thal = st.number_input(
        "Thal (0=normal,1=fixed,2=reversible)",
        min_value=0, max_value=2
    )

    if st.button("Predict Heart Disease"):
        if patient_name.strip() == "":
            st.warning("Please enter Patient Name")
        else:
            sex_val = 1 if sex == "Male" else 0

            input_data = np.array([[
                age, sex_val, cp, trestbps, chol,
                fbs, restecg, thalach, exang,
                oldpeak, slope, ca, thal
            ]])

            prediction = heart_model.predict(input_data)

            if prediction[0] == 1:
                result_text = "POSITIVE (Heart Disease Detected)"
                st.error("❌ Heart Disease Detected")
            else:
                result_text = "NEGATIVE (No Heart Disease)"
                st.success("✅ No Heart Disease Detected")

            pdf_file = generate_pdf(
                patient_name,
                patient_age,
                patient_gender,
                "Heart Disease",
                result_text
            )

            with open(pdf_file, "rb") as f:
                st.download_button(
                    "⬇️ Download Medical Report (PDF)",
                    f,
                    file_name="heart_disease_medical_report.pdf",
                    mime="application/pdf"
                )

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption(
    "© Developed by Rahul Nayak ")
