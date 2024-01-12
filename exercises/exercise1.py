import pandas as pd
from sqlalchemy import String, TEXT, INTEGER, Float, DECIMAL

#loading from data souce
datafield = pd.read_csv('https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv',sep=";", on_bad_lines='skip')

#changing column types
columnTypes = {'column_1': INTEGER, 'column_2': String, 'column_3': String, 'column_4': String, 'column_5': String,
               'column_6': String, 'column_7': Float,'column_8': Float, 'column_9': INTEGER, 'column_10': Float,
               'column_11': TEXT,'column_12': String, 'geo_punkt': DECIMAL}

#saving table to sqlite file
datafield.to_sql('airports','sqlite:///airports.sqlite', if_exists='replace', index=False)