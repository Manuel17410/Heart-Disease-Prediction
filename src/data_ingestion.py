import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion started with bucket: {self.bucket_name}, file: {self.file_name}")

    def download_csv_from_gcp(self):
        try:
            logger.info(f"Connecting to GCP with bucket: {self.bucket_name}")
            logger.info(f"Trying to download file: {self.file_name}")
            logger.info(f"Saving to: {RAW_FILE_PATH}")

            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            if not bucket.exists():
                raise CustomException(f"Bucket '{self.bucket_name}' does not exist", None)

            blob = bucket.blob(self.file_name)

            if not blob.exists():
                raise CustomException(f"The file '{self.file_name}' does not exist in bucket '{self.bucket_name}'", None)

            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"CSV file successfully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.exception("Error while downloading the CSV file")
            raise CustomException("Failed to download CSV file", e)

    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data = pd.read_csv(RAW_FILE_PATH)

            train_data, test_data = train_test_split(data, test_size=1 - self.train_test_ratio, random_state=42)

            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data into training and test sets", e)

    def run(self):
        try:
            logger.info("Starting data ingestion process")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data ingestion completed successfully")

        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")

        finally:
            logger.info("Data ingestion completed")


if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)
    data_ingestion = DataIngestion(config)
    data_ingestion.run()
