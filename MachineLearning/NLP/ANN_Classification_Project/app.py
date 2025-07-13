import streamlit as st
import pickle
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model

## Loading the model
model = load_model('model.keras')


## OPening all the encoders

with open('OneHotEncoder.pkl', 'rb') as file:
    OHE = pickle.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

## Streamlit App

st.title('Customer Churn Prediction')

geography = st.selectbox('Geography', OHE.categories_[0])
gender = st.selectbox('Gender', label_encoder.classes_)
age = st.slider('Age', 18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input("Estimated Salary")
tenure = st.slider('Tenure', 1,10)
num_of_products = st.slider('Number of Products', 1,4)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member',[0,1])


input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder.transform([gender])[0]],
    'Age':[age],
    'Tenure' : [tenure],
    'Balance' : [balance],
    'NumOfProducts' :[num_of_products],
    'HasCrCard' : [has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary' : [estimated_salary]

})

## one hot encoding
geo_encoded = OHE.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns = OHE.get_feature_names_out(['Geography']))

input_data = pd.concat([input_data.reset_index(drop=True),geo_encoded_df],axis=1)

##scaling

scaled_data = scaler.transform(input_data)

prediction = model.predict(scaled_data)
prob = prediction[0][0]

st.write(f'Churn Probability, {prob:.2f}')

if prob > 0.5:
    st.write("likely to churn")
else:
    st.write("not likely to churn")
