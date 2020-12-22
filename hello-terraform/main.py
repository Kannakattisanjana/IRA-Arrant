#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import Instance, AwsProvider
from imports.terraform_aws_modules.vpc.aws import Vpc
#import Vpc from './.gen/providers/aws';
#from './.gen/providers/aws' import Vpc
from feth import parseresourceyaml



class MyStack(TerraformStack):
  def __init__(self, scope: Construct, ns: str):
    super().__init__(scope, ns)
    resourcedetails = parseresourceyaml()
    print(" after readding from the yaml", resourcedetails)
    print("resorce region is",resourcedetails["customerName"]["region"])

    #AwsProvider(self, 'Aws', region='us-east-1')
    AwsProvider(self, 'Aws', region=resourcedetails["customerName"]["region"])


    helloInstance = Instance(self, 'hello',
      ami="ami-2757f631",
      instance_type="t2.micro",
      tags={"Name": "Provisioned by Python", "Creator": "CDKTF-Python"}

    )

    Vpc(self, 'CustomVpc',
        name='custom-vpc',
        cidr='10.0.0.0/16',
        azs=["us-east-1a", "us-east-1b"],
        public_subnets=["10.0.1.0/24", "10.0.2.0/24"]
        )

    TerraformOutput(self, 'hello_public_ip',
      value=helloInstance.public_ip
    )

app = App()
MyStack(app, "hello-terraform")


app.synth()


