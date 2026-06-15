import pandas as pd
import numpy as np

np.random.seed(42)

states = [
    "Maharashtra",
    "Delhi",
    "Uttar Pradesh",
    "Karnataka",
    "Tamil Nadu",
    "Gujarat"
]

dates = pd.date_range(
    start="2020-01-01",
    end="2022-12-31"
)

data = []

for date in dates:

    for state in states:

        confirmed = np.random.randint(
            1000,
            50000
        )

        recovered = int(
            confirmed * np.random.uniform(
                0.75,
                0.95
            )
        )

        deaths = int(
            confirmed * np.random.uniform(
                0.01,
                0.05
            )
        )

        vaccinations = np.random.randint(
            5000,
            100000
        )

        data.append([
            date,
            state,
            confirmed,
            recovered,
            deaths,
            vaccinations
        ])

df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "State",
        "Confirmed",
        "Recovered",
        "Deaths",
        "Vaccinations"
    ]
)

df.to_csv(
    "covid_india.csv",
    index=False
)

print("Dataset created")