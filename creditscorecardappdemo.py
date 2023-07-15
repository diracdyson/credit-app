"""""
-------------------------------------
@Author: Brandonlee Santos
@Date: 06_21_23
/// streamlit credit application prediction
-------------------------------------
"""""
import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Credit card approval prediction
This app predicts if an applicant will be approved for a credit card or not. Just fill in the following information and click on the Predict button.
""")

#Gender input
st.write("""
## Gender
""")
input_gender = st.radio('Select you gender',['Male','Female'], index=0)


# Age input slider
st.write("""
## Age
""")
input_age = np.negative(st.slider('Select your age', value=42, min_value=18, max_value=70, step=1) * 365.25)




# Marital status input dropdown
st.write("""
## Marital status
""")

marital_status_key = ['Married', 'Single/not married', 'Civil marriage', 'Separated', 'Widowed']
marital_status_values = np.arange(0,len(marital_status_key),1)
marital_status_dict = dict(zip(marital_status_key,marital_status_values))
input_marital_status_key = st.selectbox('Select your marital status', marital_status_key)
input_marital_status_val = marital_status_dict.get(input_marital_status_key)


# Family member count
st.write("""
## Family member count
""")
fam_member_count = float(st.selectbox('Select your family member count', [1,2,3,4,5,6]))


# Dwelling type dropdown
st.write("""
## Housing type
""")

dwelling_type_key = ['House / apartment', 'Live with parents', 'Municipal apartment ', 'Rented apartment', 'Office apartment', 'Co-op apartment']
dwelling_type_values = np.arange(0,len(dwelling_type_key),1)
dwelling_type_dict = dict(zip(dwelling_type_key,dwelling_type_values))
input_dwelling_type_key = st.selectbox('Select the type of dwelling you reside in', dwelling_type_key)
input_dwelling_type_val = dwelling_type_dict.get(input_dwelling_type_key)


# Income
st.write("""
## Income
""")
input_income = np.int(st.text_input('Enter your income (in USD)',0))


# Employment status dropdown
st.write("""
## Employment status
""")

employment_status_key = ['Working','Commercial associate','Pensioner','State servant','Student']
employment_status_values = np.arange(0,len(employment_status_key),1)
employment_status_dict = dict(zip(employment_status_key,employment_status_values))
input_employment_status_key = st.selectbox('Select your employment status', employment_status_key)
input_employment_status_val = employment_status_dict.get(input_employment_status_key)


# Employment length input slider
st.write("""
## Employment length
""")
input_employment_length = np.negative(st.slider('Select your employment length', value=6, min_value=0, max_value=30, step=1) * 365.25)


# Education level dropdown
st.write("""
## Education level
""")

edu_level_key = ['Secondary school','Higher education','Incomplete higher','Lower secondary','Academic degree']
edu_level_values = np.arange(0,len(edu_level_key),1)
edu_level_dict = dict(zip(edu_level_key,edu_level_values))
input_edu_level_key = st.selectbox('Select your education status', edu_level_key)
input_edu_level_val = edu_level_dict.get(input_edu_level_key)


# Car ownship input
st.write("""
## Car ownship
""")
input_car_ownship = st.radio('Do you own a car?',['Yes','No'], index=0)

# Property ownship input
st.write("""
## Property ownship
""")
input_prop_ownship = st.radio('Do you own a property?',['Yes','No'], index=0)


# Work phone input
st.write("""
## Work phone
""")
input_work_phone = st.radio('Do you have a work phone?',['Yes','No'], index=0)
work_phone_dict = {'Yes':1,'No':0}
work_phone_val = work_phone_dict.get(input_work_phone)

# Phone input
st.write("""
## Phone
""")
input_phone = st.radio('Do you have a phone?',['Yes','No'], index=0)
work_dict = {'Yes':1,'No':0}
phone_val = work_dict.get(input_phone)

# Email input
st.write("""
## Email
""")
input_email = st.radio('Do you have an email?',['Yes','No'], index=0)
email_dict = {'Yes':1,'No':0}
email_val = email_dict.get(input_email)





