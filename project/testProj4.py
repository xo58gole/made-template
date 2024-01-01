import unittest
import os
import pandas as pd

class TestDataPipeline(unittest.TestCase):
    def test_data_pipeline(self):
        # Execute the data pipeline
        os.system("pipeline.sh")
        print("Success: Data pipeline executed")

class TestFilesAndColumns(unittest.TestCase):
    def test_data_files_exist(self):
        self.assertTrue(os.path.exists('data/employment_data_transformed.db'))
        self.assertTrue(os.path.exists('data/language_data_transformed.db'))
        print("Success: Output files exist")

    def test_data_columns(self):
        employment_data = pd.read_csv("data/employment_data_transformed.db", encoding='utf-16-le')
        language_data = pd.read_csv("data/language_data_transformed.db", encoding='utf-16-le')
        self.assertGreater(len(employment_data.columns), 0)
        self.assertGreater(len(language_data.columns), 0)
        print("Success: Data columns test passed")

if __name__ == '__main__':
    unittest.main()