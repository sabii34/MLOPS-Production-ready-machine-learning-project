import os
import sys
import pymongo
import certifi

from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
from us_visa.exception import USvisaException
from us_visa.logger import logging

ca = certifi.where()


class MongoDBClient:
    """
    Provides a MongoDB client connection.
    - Uses TLS only for non-local URIs (e.g., MongoDB Atlas).
    - Skips TLS for localhost/127.0.0.1 (typical local MongoDB).
    """

    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                if not mongo_db_url:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

                # Local MongoDB (no TLS)
                if "localhost" in mongo_db_url or "127.0.0.1" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    # Cloud MongoDB (TLS)
                    MongoDBClient.client = pymongo.MongoClient(
                        mongo_db_url,
                        tlsCAFile=ca
                    )

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

            logging.info("MongoDB connection successful")

        except Exception as e:
            raise USvisaException(e, sys)
