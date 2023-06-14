import streamlit as st
import pickle
import pandas as pd
pipe = pickle.load(open('classifier_Naive_Bayes.pkl','rb'))
feat = pickle.load(open('feature_extraction.pkl','rb'))
st.title('NLP-SPAM-DETECTION')
col1 = st.columns(1)

title = st.text_input('Enter the String', 'Ex:Greeting...')

if st.button('Predict Spam or Ham'):
    title = [title]
    input_data_features = feat.transform(title)
    prediction = pipe.predict(input_data_features)
    if (prediction[0]==1):
        st.header("Ham mail")
    else:
        st.header("Spam mail")
