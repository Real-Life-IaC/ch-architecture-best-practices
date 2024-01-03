"""
This is an example from the CDK documentation on how to share buckets between stacks.

https://docs.aws.amazon.com/cdk/api/v1/docs/aws-s3-readme.html#sharing-buckets-between-stacks
I do not recommend following this approach for the reasons listed in the book.
"""

import aws_cdk as cdk

from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from constructs import Construct


class BadProducerStack(cdk.Stack):
    """Define the bucket"""

    def __init__(
        self,
        scope: Construct,
        id: str,
    ) -> None:
        super().__init__(scope, id)

        self.bucket = s3.Bucket(scope=self, id="MyBucket")


class BadConsumerStack(cdk.Stack):
    """Consume the bucket"""

    def __init__(
        self,
        scope: Construct,
        id: str,
        bucket: s3.Bucket,
    ) -> None:
        super().__init__(scope, id)

        self.user = iam.User(scope=self, id="MyUser")

        bucket.grant_read(self.user)
