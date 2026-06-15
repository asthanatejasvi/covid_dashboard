import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from utils import load_data

df = load_data()

daily = df.groupby(
    "Date"
)["Confirmed"].sum().reset_index()

daily["Day"] = np.arange(
    len(daily)
)

X = daily[["Day"]]

y = daily["Confirmed"]

model = LinearRegression()

model.fit(X,y)

future = np.arange(
    len(daily),
    len(daily)+30
).reshape(-1,1)

pred = model.predict(
    future
)

forecast = pd.DataFrame({
    "Day":future.flatten(),
    "Prediction":pred
})

st.title(
    "COVID Forecast"
)

fig = px.line(
    forecast,
    x="Day",
    y="Prediction"
)

st.plotly_chart(
    fig,
    use_container_width=True
)