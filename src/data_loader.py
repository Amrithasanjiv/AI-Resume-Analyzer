from pathlib import Path
import pandas as pd

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "raw" / "Resume.csv"


def load_dataset():
    return pd.read_csv(DATA_PATH)