import requests
import os
import pandas as pd
#import chardet

# Define the URLs for the data sets
data_urls = {
    "Employment of Migrants": "https://opendata.leipzig.de/dataset/ac13f1cd-1515-47df-bc6f-ec18ae325918/resource/10e95615-f843-4b9f-8712-60e7be53eb5f/download/abb9erwerbstatigkeitmigratinnen.csv",
    "Language Understanding of Migrants": "https://opendata.leipzig.de/dataset/126ea2a3-38f4-410d-91fe-c683558c99cd/resource/c269e8b9-9adf-4202-ad15-14317a505691/download/abb8sprachverstandnis.csv"
}

# Create a directory to store the data
data_directory = 'data'
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Function to download and save the data
def download_and_save_data(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# Download and save the data sets
for data_name, data_url in data_urls.items():
    file_path = f"{data_directory}/{data_name.replace(' ', '_').lower()}.csv"
    download_and_save_data(data_url, file_path)
    print(f"{data_name} downloaded and saved to {file_path}")

# Load the data from the CSV files into pandas dataframes with the correct encoding
employment_data = pd.read_csv("data/employment_of_migrants.csv", encoding='UTF-16')
language_data = pd.read_csv("data/language_understanding_of_migrants.csv", encoding='EUC-KR')

#with open("data/language_understanding_of_migrants.csv", 'rb') as file:
    #result = chardet.detect(file.read())

#encoding = result['encoding']
#print(f"Detected encoding: {encoding}")

# Print the columns of each DataFrame to check the actual column names
print("Employment Data Columns:", employment_data.columns)
print("Language Data Columns:", language_data.columns)

# Transform Employment of Migrants data
employment_data_transformed = employment_data.rename(columns={
    'Region': 'region',
    'männlich': 'männlich',
    'weiblich': 'weiblich'
})

# Store the transformed Employment of Migrants data in a new CSV file
employment_data_transformed.to_csv("C:/Users/49157/PycharmProjects/made-template/data/transformed_employment_data.csv", index=False)

# Transform Language Understanding of Migrants data
language_data_transformed = language_data.rename(columns={
    'Gebiet': 'Gebiet',
    'deutsch verstehen männlich': 'deutsch_verstehen_maennlich',
    'deutsch sprechen männlich': 'deutsch_sprechen_maennlich',
    'deutsch verstehen weiblich': 'deutsch_verstehen_weiblich',
    'deutsch sprechen weiblich': 'deutsch_sprechen_weiblich'
})

# Store the transformed Language Understanding of Migrants data in a new CSV file
language_data_transformed.to_csv("C:/Users/49157/PycharmProjects/made-template/data/transformed_language_data.csv", index=False)
