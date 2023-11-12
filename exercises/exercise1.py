import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import csv
from io import StringIO

url = "csv.csv"
data = []

# Read the file line by line, handling any problematic lines
with open(url, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        try:
            line_str = ",".join(line)
            data.append(pd.read_csv(StringIO(line_str), header=None))
        except pd.errors.ParserError:
            pass  # Skip problematic lines

# Concatenate the data into a DataFrame
df = pd.concat(data)

engine = create_engine("sqlite:///airports.sqlite")
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS airports (
            column_1 INTEGER PRIMARY KEY,
            column_2 TEXT,
            column_3 TEXT,
            column_4 TEXT,
            column_5 TEXT,
            column_6 TEXT,
            column_7 FLOAT,
            column_8 FLOAT,
            column_9 FLOAT,
            column_10 TEXT,
            column_11 TEXT,
            column_12 TEXT,
            geo_punkt TEXT
        )
    """))

    df.to_sql("airports", engine, if_exists="replace", index=False)
