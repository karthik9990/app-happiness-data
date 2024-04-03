import streamlit as st
import plotly.express as px
import pandas as pd


st.header("In Search of Happiness")
option1 = st.selectbox("Select the data for X-axis:",
                       ("GDP", "Happiness", "Generosity"))

option2 = st.selectbox("Select the data for Y-axis:",
                       ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

match option1:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match option2:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{option1} and {option2}")

figure = px.scatter(x=x_array, y=y_array, labels={"X":option1, "Y": option2})
st.plotly_chart(figure)
