import os
import boto3

from us_visa.constants import (
    AWS_SECRET_ACCESS_KEY_ENV_KEY,
    AWS_ACCESS_KEY_ID_ENV_KEY,
    REGION_NAME,
)
from us_visa.exception import USvisaException


class S3Client:
    s3_client = None
    s3_resource = None

    def __init__(self, region_name: str = REGION_NAME):
        """
        Reads AWS creds from environment variables and creates boto3 client/resource.
        """

        try:
            if S3Client.s3_resource is None or S3Client.s3_client is None:
                access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
                secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

                if not access_key_id:
                    raise Exception(
                        f"Environment variable {AWS_ACCESS_KEY_ID_ENV_KEY} is not set."
                    )
                if not secret_access_key:
                    raise Exception(
                        f"Environment variable {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set."
                    )

                S3Client.s3_resource = boto3.resource(
                    "s3",
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name=region_name,
                )

                S3Client.s3_client = boto3.client(
                    "s3",
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name=region_name,
                )

            self.s3_resource = S3Client.s3_resource
            self.s3_client = S3Client.s3_client

        except Exception as e:
            raise USvisaException(e, None)
