import aws_cdk as cdk

from constructs import Construct
from constructs_package.org_s3 import OrgBucket


class MyStack(cdk.Stack):
    """Define the bucket"""

    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        OrgBucket(
            scope=self,
            id="MyBucket",
        )
