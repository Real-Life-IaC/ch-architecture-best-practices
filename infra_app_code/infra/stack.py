import aws_cdk as cdk

from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from constructs import Construct


class MyStack(cdk.Stack):
    """Creates a Stack with a bucket and a lambda"""

    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            scope=self,
            id="MyBucket",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        function = _lambda.DockerImageFunction(
            scope=self,
            id="MyFunction",
            code=_lambda.DockerImageCode.from_image_asset(
                directory="app",
            ),
            environment={
                "BUCKET_NAME": bucket.bucket_name,
            },
        )

        bucket.grant_write(function)
