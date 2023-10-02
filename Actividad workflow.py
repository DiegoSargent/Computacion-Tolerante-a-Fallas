from prefect import Flow, task
import pandas as pd

@task
def extract_data():
    return pd.read_csv("source_data.csv")

@task
def transform_data(data):
    # Perform data transformation here
    return transformed_data

@task
def load_data(data):
    # Load data to a database or file
    pass

# Definir el flujo de trabajo directamente en el nivel del archivo
with Flow("Simple ETL") as flow:
    data = extract_data()
    transformed = transform_data(data)
    load_data(transformed)

# Ejecutar el flujo de trabajo si el archivo se ejecuta como script principal
if __name__ == "__main__":
    flow.run()
