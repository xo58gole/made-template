import pandas as pd
import csv
from sqlalchemy import create_engine, inspect
from sqlite3 import connect

# Correct the delimiter and quotechar
with open('csv.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in spamreader:
        print(', '.join(row))

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
with open('csv.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(spamreader)  # skip header row
    for row in spamreader:
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
