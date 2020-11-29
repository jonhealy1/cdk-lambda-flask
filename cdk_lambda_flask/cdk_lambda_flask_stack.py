import os

from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


class CdkLambdaFlaskStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        flask_handler = _lambda.Function(
            self, 'FlaskHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda/' + os.environ["ZAPPA_LAMBDA_PACKAGE"]),
            handler='handler.lambda_handler',
            timeout=core.Duration.seconds(15),
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=flask_handler,
        )
