from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Localizar el dataset
project_path = Path(__file__).resolve().parent.parent
data_folder = project_path / "data"

csv_files = list(data_folder.glob("*.csv"))

if len(csv_files) != 1:
    raise FileNotFoundError("Se esperaba un único archivo CSV en data/")

# Cargar datos
df = pd.read_csv(csv_files[0], low_memory=False)

print("GLOBAL SECURITY INTELLIGENCE")
print("=" * 40)

# Comprobar las variables necesarias
required_columns = ["year", "country", "id"]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Faltan columnas: {missing_columns}")

# Seleccionar acontecimientos de 2025
df_2025 = df[df["year"] == 2025]

# Contar acontecimientos por país
top_countries = (
    df_2025.groupby("country")["id"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 COUNTRIES BY RECORDED EVENTS — 2025")
print(top_countries)

# Evolución anual
annual_events = (
    df[df["year"].between(2015, 2025)]
    .groupby("year")["id"]
    .nunique()
    .sort_index()
)

print("\nGLOBAL EVENT TRENDS — 2015–2025")
print(annual_events)

print("\nAnalysis completed!")

# Crear carpeta para guardar gráficos

charts_folder = project_path / "data" / "charts"

charts_folder.mkdir(parents=True, exist_ok=True)

# Gráfico: países con más acontecimientos en 2025

plt.figure(figsize=(12, 7))

top_countries.sort_values().plot(

    kind="barh",

    color="#2563EB"

)

plt.title(

    "Top 10 Countries by Recorded Organized Violence Events (2025)",

    fontsize=14,

    fontweight="bold"

)

plt.xlabel("Number of Recorded Events")

plt.ylabel("Country")

plt.tight_layout()

# Guardar gráfico

chart_path = charts_folder / "top_10_countries_2025.png"

plt.savefig(chart_path, dpi=300)

plt.show()

print(f"\nChart saved to: {chart_path}")

# Gráfico 2: evolución anual de acontecimientos

plt.figure(figsize=(12, 6))

plt.plot(
    annual_events.index,
    annual_events.values,
    marker="o",
    linewidth=2.5,
    color="#2563EB"
)

plt.title(
    "Global Organized Violence Events (2015–2025)",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Year")
plt.ylabel("Number of Recorded Events")

plt.grid(True, alpha=0.3)
plt.xticks(range(2015, 2026))

plt.tight_layout()

# Guardar el segundo gráfico
trend_path = charts_folder / "global_conflict_trends_2015_2025.png"

plt.savefig(trend_path, dpi=300)
plt.close()

print(f"Trend chart saved to: {trend_path}")