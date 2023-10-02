import requests
import json
from collections import namedtuple
from contextlib import closing
import sqlite3
from prefect import task, Flow

# Task para extraer datos
@task
def extract_data():
    url = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1"
    params = {'size': 10}
    response = requests.get(url, params=params)
    response_json = json.loads(response.text)
    return response_json['hits']['hits']

# Task para transformar datos
@task
def transform_data(raw_data):
    complaints = []
    Complaint = namedtuple('Complaint', ['data_received', 'state', 'product', 'company', 'complaint_what_happened'])
    
    for row in raw_data:
        source = row.get('_source')
        complaint = Complaint(
            data_received=source.get('date_received'),
            state=source.get('state'),
            product=source.get('product'),
            company=source.get('company'),
            complaint_what_happened=source.get('complaint_what_happened')
        )
        complaints.append(complaint)
    
    return complaints

# Task para cargar datos
@task
def load_data(parsed_data):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS complaint (
        timestamp TEXT,
        state TEXT,
        product TEXT,
        company TEXT,
        complaint_what_happened TEXT
    )
    '''
    insert_data_sql = '''
    INSERT INTO complaint
    VALUES (?, ?, ?, ?, ?)
    '''

    with closing(sqlite3.connect("cfpbcomplaints.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.executescript(create_table_sql)
            cursor.executemany(insert_data_sql, parsed_data)
            conn.commit()

# Creación del flujo
with Flow("CFPB Complaints ETL") as flow:
    raw_data = extract_data()
    parsed_data = transform_data(raw_data)
    load_data(parsed_data)

# Ejecución del flujo
flow.run()
