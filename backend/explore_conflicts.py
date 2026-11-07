from pathlib import Path
import pandas as pd

# 1. Localizar la carpeta de datos
project_path = Path(__file__).resolve().parent.parent
data_folder = project_path / "data"

# 2. Buscar el archivo CSV
csv_files = list(data_folder.glob("*.csv"))

if len(csv_files) != 1:
    raise FileNotFoundError(
        f"Se esperaba un CSV en {data_folder}, "
        f"pero se encontraron {len(csv_files)}."
    )

csv_path = csv_files[0]

print("NATIONAL SECURITY INTELLIGENCE")
print("--------------------------------")
print("Dataset:", csv_path.name)

# 3. Cargar los datos
df = pd.read_csv(csv_path, low_memory=False)

# 4. Información general
print("\nDATASET OVERVIEW")
print("Total events:", len(df))
print("Total columns:", len(df.columns))

# 5. Mostrar las columnas
print("\nAVAILABLE VARIABLES")
print(df.columns.tolist())

# 6. Mostrar los primeros registros
print("\nFIRST FIVE RECORDS")
print(df.head().to_string(index=False))

# 7. Comprobar valores ausentes
print("\nMISSING VALUES")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\nInitial data exploration completed!")