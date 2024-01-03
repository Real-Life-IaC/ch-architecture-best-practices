import aws_cdk as cdk

from infra.stack import MyStack


app = cdk.App()
MyStack(app, "MyStack")
app.synth()
