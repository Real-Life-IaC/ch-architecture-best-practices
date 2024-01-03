import aws_cdk as cdk

from stack import MyStack


app = cdk.App()

MyStack(
    scope=app,
    id="MyStack-Sandbox",
    env=cdk.Environment(
        account="123456789012",
        region="us-east-1",
    ),
)

MyStack(
    scope=app,
    id="MyStack-Staging",
    env=cdk.Environment(
        account="123123123123",
        region="us-east-1",
    ),
)

MyStack(
    scope=app,
    id="MyStack-Production",
    env=cdk.Environment(
        account="456456456456",
        region="us-east-1",
    ),
)

app.synth()
