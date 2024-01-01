import unittest
import os


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

    

if __name__ == '__main__':
    unittest.main()
