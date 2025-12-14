from pathlib import Path
from src.data.ingestion import load_csv, save_raw_data

df = load_csv(Path("data/samples/sample.csv"))
save_raw_data(df, "sample_copy.csv")
