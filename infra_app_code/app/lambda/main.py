import json
import os

import boto3
import requests

from mypy_boto3_s3 import S3Client


BUCKET_NAME = os.getenv("BUCKET_NAME", "bucket-name")
s3_client: S3Client = boto3.client("s3")


def handler(event: dict, context: dict) -> dict:
    """Handle the request."""

    # get a response from httpbin
    response = requests.get(
        url="https://httpbin.org/get",
        headers={"Accept": "application/json"},
        timeout=5,
    )
    response.raise_for_status()
    data = response.json()

    # upload the response to S3
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key="response.json",
        Body=json.dumps(data).encode("utf-8"),
    )

    # return the response
    return {
        "statusCode": 200,
        "body": data,
    }
