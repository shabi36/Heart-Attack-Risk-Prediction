import streamlit as st
import pickle
import numpy as np


dataset = pickle.load(open("HEART_ATTACK_RISK_DATASET.pkl", "rb"))
pipe = pickle.load(open("pipe_HEART_ATTACK_RISK.pkl", "rb"))


st.title("HEART ATTACK RISK PREDICTION")


def fetch_binary(x):
    if x == "Yes":
        return 1
    return 0



col1 , col2 = st.columns(2)
with col1:
    #age
    age = st.number_input("Age" , min_value=0 )

with col2:
    #gender
    gend = st.selectbox("Gender" , dataset["Gender"].unique())





col1 , col2 = st.columns(2)
with col1:
    #cholesteral
    chol = st.number_input("Cholesterol Levels" , min_value=0)

with col2:
    #Heart rate
    hr = st.number_input("Heart Rate (bpm) ", min_value=0)




col1 , col2 = st.columns(2)
with col1:
    #bp - systolic
    bps = st.number_input("Blood Pressure - Systolic (mm Hg)" , min_value=0)

with col2:
    #bp - diastolic
    bpd = st.number_input("Blood Pressure - Diastolic (mm Hg)" , min_value=0)





col1 , col2 = st.columns(2)
with col1:
    #diet
    diet = st.selectbox("Diet " , dataset["Diet"].unique())

with col2:
    #body mass index
    bmi = st.number_input("Body Mass Index" )





col1 , col2 = st.columns(2)
with col1:
    #triglycerides
    tri = st.number_input("Triglycerides ( mg/dl)")

with col2:
    #sleeping hours per day
    sleep = st.number_input("Sleeping hours per day" , min_value=0)





col1 , col2 = st.columns(2)
with col1:
    #stress level
    stress = st.number_input("Stress Level",min_value=0 , max_value=10)

with col2:
    #medication use 1 - yes , 0-no
    medi = st.selectbox("Any medication use?" , ["Yes","No"])

medi = fetch_binary(medi)



#physical activity days per week
act = st.number_input("How many days per week does the patient is involed in any physical activities?" , min_value=0)



#smoking 1-yes , 0 - no
smo = st.selectbox("Does the patient smoke?" , ["Yes","No"])
smo = fetch_binary(smo)





#obesity 1-yes , 0 - no
obe = st.selectbox("Does the patient have high Obesity?" , ["Yes","No"])

obe = fetch_binary(obe)





#alcohol 1-yes , 0 - no
alco = st.selectbox("Does the patient consume alcohol?" , ["Yes","No"])

alco = fetch_binary(alco)





#excercie hours per week
excer = st.number_input("How many hours a week does the patient exercise?")



#sedentary hours per day
sed = st.number_input("What are the sedentary hours a day of the patient?")




#diabetes 1-yes , 0 - no
dia = st.selectbox("Does the patient have Diabetes?" , ["Yes","No"])

dia = fetch_binary(dia)




#previous heart problems 1-yes , 0-no
heartp = st.selectbox("Does the patient have any previos heart problems?", ["No" , "Yes"])
if heartp == "Yes":
    heartp_type = st.text_area("Describe the heart problem? (Optional)")

heartp = fetch_binary(heartp)

#family history 1-yes , 0 - no
fh = st.selectbox("Does anybody in the patient's family have any history of Heart Attack? ", ["Yes","No"])

fh = fetch_binary(fh)


if st.button("Predict Heart Attack Risk"):
    query = np.array([age,gend,chol,bps,bpd,hr,dia,fh,smo,obe,alco,excer,
                      diet,heartp,medi,stress,sed,bmi,tri,act,sleep])

    query = query.reshape(1, 21)

    x = pipe.predict(query)[0]


    if x == 1:
        st.title("High Heart Attack Risk ")

    else:
        st.title("Low Heart Attack Risk")