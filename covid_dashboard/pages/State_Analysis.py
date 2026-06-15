import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

state = st.selectbox(
    "Choose State",
    sorted(df["State"].unique())
)

state_df = df[
    df["State"] == state
]

st.title(
    f"{state} Analysis"
)

fig = px.line(
    state_df,
    x="Date",
    y="Confirmed"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.bar(
    state_df.groupby("Date")[
        "Vaccinations"
    ].sum().reset_index(),
    x="Date",
    y="Vaccinations"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)