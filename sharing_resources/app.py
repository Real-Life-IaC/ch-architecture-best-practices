import aws_cdk as cdk

from bad_stack import BadConsumerStack
from bad_stack import BadProducerStack
from stack import ConsumerStack
from stack import ProducerStack


app = cdk.App()

producer_stack = BadProducerStack(
    scope=app,
    id="BadProducerStack",
)

BadConsumerStack(
    scope=app,
    id="BadConsumerStack",
    bucket=producer_stack.bucket,
)


producer_stack = ProducerStack(
    scope=app,
    id="ProducerStack",
)

ConsumerStack(
    scope=app,
    id="ConsumerStack",
)

app.synth()
