import csv
import requests
from sqlite3 import connect

# Read CSV file from URL
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
response = requests.get(url)
decoded_content = response.content.decode('utf-8')
csv_reader = csv.reader(decoded_content.splitlines(), delimiter=',')
header = next(csv_reader)  # get header row
print(f"Number of columns: {len(header)}")

# Define SQLite database connection and create table
conn = connect("airports.sqlite")
cursor = conn.cursor()
cursor.execute("""
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
""")

# Write data to SQLite table
for row in csv_reader:
    cursor.execute("""
        INSERT INTO airports (
            column_1,
            column_2,
            column_3,
            column_4,
            column_5,
            column_6,
            column_7,
            column_8,
            column_9,
            column_10,
            column_11,
            column_12,
            geo_punkt
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, row)

# Commit changes and close connection
conn.commit()
conn.close()