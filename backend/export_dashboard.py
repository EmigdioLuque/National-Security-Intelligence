from pathlib import Path
import json
import pandas as pd

# Localizar las carpetas del proyecto
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "data"

# Buscar el dataset
csv_files = list(data_folder.glob("GED*.csv"))

if not csv_files:
    raise FileNotFoundError("No se encontró el dataset UCDP.")

csv_path = csv_files[0]

print("Loading UCDP dataset...")

# Cargar únicamente las columnas necesarias
df = pd.read_csv(
    csv_path,
    usecols=["id", "year", "country"],
    low_memory=False
)

# Seleccionar el periodo de análisis
df = df[df["year"].between(2015, 2025)]

# Calcular acontecimientos por año
annual_events = (
    df.groupby("year")
    .size()
    .sort_index()
)

# Calcular los diez países con más acontecimientos en 2025
top_countries = (
    df[df["year"] == 2025]
    .groupby("country")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

# Preparar datos para la web
dashboard_data = {
    "source": "UCDP GED 26.1",
    "period": "2015-2025",
    "total_events": int(len(df)),
    "countries_analyzed": int(df["country"].nunique()),
    "annual_events": [
        {"year": int(year), "events": int(events)}
        for year, events in annual_events.items()
    ],
    "top_countries_2025": [
        {"country": country, "events": int(events)}
        for country, events in top_countries.items()
    ],
    "country_annual_events": [

    {

        "country": country,

        "year": int(year),

        "events": int(events)

    }

    for (country, year), events in (

        df.groupby(["country", "year"])

        .size()

        .items()

    )

]
}

# Guardar JSON
output_path = data_folder / "dashboard_data.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(dashboard_data, file, indent=4, ensure_ascii=False)

print(f"Dashboard data exported to: {output_path}")
print("Export completed!")