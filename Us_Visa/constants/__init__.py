import os
from datetime import date

DB_NAME="US_VISA"

COLLECTION_NAME="visa_dataset"

CONNECTION_URL="mongodb+srv://sabashahbaz731_db_user:uWSV0cgHHFf5bUTq@cluster0.k7889eq.mongodb.net/?appName=Cluster0"

PIPLINE_NAME: str = "us_visa_pipeline"
ARTIFACTS_DIR: str = "artifacts"

MODEL_FILE_NAME: str = "model.pkl"

# data ingestion related constants start with DATA INGESTION VAR NAME
DATA_INGESTION_COLLECTION_NAME: str = "visa_data_collection"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2


