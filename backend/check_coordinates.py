from pathlib import Path
import pandas as pd

# Project paths
project_folder = Path(__file__).resolve().parent.parent
data_path = project_folder / "data" / "GEDEvent_v26_1.csv"

# Load only the columns needed for the map
columns = [
    "id",
    "date_start",
    "country",
    "latitude",
    "longitude",
    "type_of_violence"
]

df = pd.read_csv(
    data_path,
    usecols=columns,
    low_memory=False
)

print("\n--- GEOGRAPHIC DATA CHECK ---")

print("\nTotal events:", len(df))

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nMissing coordinates:")
print(df[["latitude", "longitude"]].isna().sum())

print("\nSample events:")
print(df.head(5).to_string(index=False))

print("\nCoordinate check completed!")