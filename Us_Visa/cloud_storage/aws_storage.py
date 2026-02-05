# us_visa/cloud_storage/aws_storage.py

import os
import sys
import pickle
from io import StringIO
from typing import Union, List, Optional

from botocore.exceptions import ClientError
from pandas import DataFrame, read_csv
from mypy_boto3_s3.service_resource import Bucket

from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.configuration.aws_connection import S3Client


class SimpleStorageService:
    """
    Wrapper class for AWS S3 operations
    """

    def __init__(self):
        try:
            s3_client = S3Client()
            self.s3_resource = s3_client.s3_resource
            self.s3_client = s3_client.s3_client
        except Exception as e:
            raise USvisaException(e, sys) from e

    # ✅ REPLACE your old method with this one
    def s3_key_path_available(self, bucket_name: str, s3_key: str) -> bool:
        """
        Check whether a given key/path exists in S3 bucket WITHOUT listing the bucket.
        This avoids needing s3:ListBucket permission.
        """
        try:
            self.s3_client.head_object(Bucket=bucket_name, Key=s3_key)
            return True
        except ClientError as e:
            code = e.response.get("Error", {}).get("Code", "")
            # Object not found cases
            if code in ("404", "NoSuchKey", "NotFound"):
                return False
            # Any other error (AccessDenied etc.)
            raise USvisaException(e, sys) from e
        except Exception as e:
            raise USvisaException(e, sys) from e

    def get_bucket(self, bucket_name: str) -> Bucket:
        try:
            return self.s3_resource.Bucket(bucket_name)
        except Exception as e:
            raise USvisaException(e, sys) from e

    def get_file_object(self, filename: str, bucket_name: str) -> Union[List[object], object]:
        """
        NOTE: This uses Bucket.objects.filter which may require ListBucket permissions.
        If you still get AccessDenied here later, tell me and we’ll rewrite it to use get_object.
        """
        try:
            bucket = self.get_bucket(bucket_name)
            file_objects = list(bucket.objects.filter(Prefix=filename))
            return file_objects[0] if len(file_objects) == 1 else file_objects
        except Exception as e:
            raise USvisaException(e, sys) from e

    @staticmethod
    def read_object(object_name: object, decode: bool = True, make_readable: bool = False):
        try:
            raw = object_name.get()["Body"].read()
            data = raw.decode() if decode else raw
            return StringIO(data) if make_readable else data
        except Exception as e:
            raise USvisaException(e, sys) from e

    def load_model(self, model_name: str, bucket_name: str, model_dir: Optional[str] = None) -> object:
        try:
            model_path = model_name if model_dir is None else f"{model_dir}/{model_name}"
            file_object = self.get_file_object(model_path, bucket_name)
            model_bytes = self.read_object(file_object, decode=False)
            return pickle.loads(model_bytes)
        except Exception as e:
            raise USvisaException(e, sys) from e

    def create_folder(self, folder_name: str, bucket_name: str):
        try:
            self.s3_client.put_object(Bucket=bucket_name, Key=f"{folder_name}/")
        except Exception as e:
            raise USvisaException(e, sys) from e

    def upload_file(self, from_filename: str, to_filename: str, bucket_name: str, remove: bool = True):
        try:
            self.s3_client.upload_file(from_filename, bucket_name, to_filename)
            if remove:
                os.remove(from_filename)
        except Exception as e:
            raise USvisaException(e, sys) from e

    def upload_df_as_csv(
        self,
        data_frame: DataFrame,
        local_filename: str,
        bucket_filename: str,
        bucket_name: str,
    ):
        try:
            data_frame.to_csv(local_filename, index=False)
            self.upload_file(local_filename, bucket_filename, bucket_name)
        except Exception as e:
            raise USvisaException(e, sys) from e

    def get_df_from_object(self, object_: object) -> DataFrame:
        try:
            content = self.read_object(object_, make_readable=True)
            return read_csv(content)
        except Exception as e:
            raise USvisaException(e, sys) from e

    def read_csv(self, filename: str, bucket_name: str) -> DataFrame:
        try:
            csv_obj = self.get_file_object(filename, bucket_name)
            return self.get_df_from_object(csv_obj)
        except Exception as e:
            raise USvisaException(e, sys) from e

