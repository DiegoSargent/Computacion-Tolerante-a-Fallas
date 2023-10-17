from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd

default_args = {
    'owner': 'tú',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'procesamiento_csv',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  )

def descargar_csv():
    print("Descargando archivo CSV...")

def procesar_datos():
    data = {'Columna1': [1, 2, 3], 'Columna2': ['A', 'B', 'C']}
    df = pd.DataFrame(data)
    print("Procesando datos:")
    print(df)

def almacenar_resultado():
    print("Almacenando resultado...")

descarga_task = PythonOperator(
    task_id='descargar_csv',
    python_callable=descargar_csv,
    dag=dag,
)

procesamiento_task = PythonOperator(
    task_id='procesar_datos',
    python_callable=procesar_datos,
    dag=dag,
)

almacenamiento_task = PythonOperator(
    task_id='almacenar_resultado',
    python_callable=almacenar_resultado,
    dag=dag,
)

descarga_task >> procesamiento_task >> almacenamiento_task
