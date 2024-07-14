import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import nltk
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import mysql.connector

# Ignore specific warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


def streamlit():
    tab1, tab2 = st.tabs(["Home", "Sentiment Analysis"])
    with tab1:
        st.markdown('<h1 style="text-align: center; color: red;">GUVI SENTIMENT ANALYSIS</h1>', unsafe_allow_html=True)
        name = st.text_input("Please enter your name", "")
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        if st.button("Login"):
            mycursor.execute(
                "INSERT INTO cust_info (name, login) VALUES (%s, %s)",
                (name, formatted_datetime)
            )
            mydb.commit()
            st.success('Data migrated to RDS-Mysql server!', icon="✅")

    with tab2:
        sentence = st.text_input("Please enter the sentence", "")

        if st.button("Sentiment Analysis"):
            with open('/home/ec2-user/rf.pkl', 'rb') as file:
                model = pickle.load(file)
            
            y_pred = model.predict(sentence)

            if y_pred:
                    st.write("Sentiment Analysis Result:")
                    for sentiment, score in y_pred:
                         st.write(f"{sentiment}: {score:.4f}")
                         st.progress(int(score * 100))



mydb = mysql.connector.connect(
    host="",
    user="user",
    password="",
    port="3080",
    )
mycursor = mydb.cursor(buffered=True)

mycursor.execute("create database if not exists sentimentanalysis")
mycursor.execute("use sentimentanalysis")
mycursor.execute("create table if not exists cust_info (name varchar(255) ,login DATETIME)")

streamlit()
