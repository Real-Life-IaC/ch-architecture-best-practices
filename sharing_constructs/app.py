import aws_cdk as cdk

from stack import MyStack


app = cdk.App()
MyStack(
    scope=app,
    id="MyStack",
    env=cdk.Environment(
        account="123456789012",
        region="us-east-1",
    ),
)
app.synth()
