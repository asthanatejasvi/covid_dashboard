from pathlib import Path
import pandas as pd

def load_data():
    file_path = Path(__file__).parent / "covid_india.csv"

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df