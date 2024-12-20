import psycopg2
import streamlit as st

conn = psycopg2.connect(
    host=st.secrets["HOST"] ,
    database=st.secrets["DATABASE"],
    user=st.secrets["USERNAME"],
    password=st.secrets["PASSWORD"])

cur = conn.cursor()