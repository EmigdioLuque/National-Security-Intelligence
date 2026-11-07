from pathlib import Path
import pandas as pd
import json

# Project paths
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "data"

input_path = data_folder / "GEDEvent_v26_1.csv"
output_path = data_folder / "map_data.json"

print("Loading geographic data...")

# Columns needed for the map
columns = [
    "id",
    "date_start",
    "country",
    "latitude",
    "longitude",
    "type_of_violence",
    "best"
]

df = pd.read_csv(
    input_path,
    usecols=columns,
    low_memory=False
)

# Convert dates
df["date_start"] = pd.to_datetime(
    df["date_start"],
    errors="coerce"
)

# Filter years 2015–2025
df = df[
    (df["date_start"].dt.year >= 2015) &
    (df["date_start"].dt.year <= 2025)
].copy()

# Remove invalid geographic coordinates
df = df.dropna(subset=["latitude", "longitude"])

df = df[
    df["latitude"].between(-90, 90) &
    df["longitude"].between(-180, 180)
]

print("Events available:", len(df))
# Calculate statistics using the complete dataset

# These statistics are calculated before sampling

full_event_count = len(df)

print("Total events in complete dataset:", full_event_count)
# Export complete statistics by country, year and violence type
df["year"] = df["date_start"].dt.year

full_statistics = (
    df.groupby(["country", "year", "type_of_violence"])
    .agg(
        events=("id", "size"),
        fatalities=("best", "sum")
    )
    .reset_index()
)

statistics_path = data_folder / "map_statistics.json"

full_statistics.to_json(
    statistics_path,
    orient="records",
    indent=2
)

print("Complete statistics exported:", statistics_path)
# Select a reproducible sample for web performance
sample_size = min(10000, len(df))

if len(df) > sample_size:
    df = df.sample(
        n=sample_size,
        random_state=42
    )

# Prepare geographic records
map_events = []

for _, row in df.iterrows():

    map_events.append({
        "id": int(row["id"]),
        "country": str(row["country"]),
        "latitude": float(row["latitude"]),
        "longitude": float(row["longitude"]),
        "date": row["date_start"].strftime("%Y-%m-%d"),
        "type_of_violence": int(row["type_of_violence"]),

"fatalities": int(row["best"]) if pd.notna(row["best"]) else None
    })

# Export JSON
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(
        map_events,
        file,
        ensure_ascii=False
    )

print("Map events exported:", len(map_events))
print("File created:", output_path)
print("Export completed!")