#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import Instance, AwsProvider


class MyStack(TerraformStack):
  def __init__(self, scope: Construct, ns: str):
    super().__init__(scope, ns)

    AwsProvider(self, 'Aws', region='us-east-1')
    helloInstance = Instance(self, 'hello',
      ami="ami-2757f631",
      instance_type="t2.micro",
      tags={"Name": "Provisioned by Python", "Creator": "CDKTF-Python"}

    )


    TerraformOutput(self, 'hello_public_ip',
      value=helloInstance.public_ip
    )

app = App()
MyStack(app, "hello-terraform")

app.synth()


