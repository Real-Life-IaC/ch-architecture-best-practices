import aws_cdk as cdk

from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_ssm as ssm
from constructs import Construct


class ProducerStack(cdk.Stack):
    """Define the bucket"""

    def __init__(
        self,
        scope: Construct,
        id: str,
    ) -> None:
        super().__init__(scope, id)

        self.bucket = s3.Bucket(scope=self, id="MyBucket")

        ssm.StringParameter(
            scope=self,
            id="MyBucketArnParameter",
            string_value=self.bucket.bucket_arn,
            parameter_name="/my-app/my-bucket/arn",
        )


class ConsumerStack(cdk.Stack):
    """Consume the bucket"""

    def __init__(self, scope: Construct, id: str) -> None:
        super().__init__(scope, id)

        bucket_arn = ssm.StringParameter.value_for_string_parameter(
            scope=self,
            parameter_name="/my-app/my-bucket/arn",
        )

        bucket = s3.Bucket.from_bucket_arn(
            scope=self,
            id="MyBucket",
            bucket_arn=bucket_arn,
        )

        self.user = iam.User(scope=self, id="MyUser")

        bucket.grant_read(self.user)
