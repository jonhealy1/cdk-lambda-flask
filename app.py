#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_flask.cdk_lambda_flask_stack import CdkLambdaFlaskStack


app = core.App()
CdkLambdaFlaskStack(app, "cdk-lambda-flask")

app.synth()
