import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("National Overview")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Cases",
    f"{df['Confirmed'].sum():,}"
)

c2.metric(
    "Recovered",
    f"{df['Recovered'].sum():,}"
)

c3.metric(
    "Deaths",
    f"{df['Deaths'].sum():,}"
)

c4.metric(
    "Vaccinations",
    f"{df['Vaccinations'].sum():,}"
)

daily = df.groupby(
    "Date"
)["Confirmed"].sum().reset_index()

fig = px.line(
    daily,
    x="Date",
    y="Confirmed"
)

st.plotly_chart(
    fig,
    use_container_width=True
)