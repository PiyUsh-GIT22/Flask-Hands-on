import json

import conf
import boto3

# create lambda client
client = boto3.client('lambda',
                      region_name=conf.region,
                      aws_access_key_id=conf.aws_access_key_id,
                      aws_secret_access_key=conf.aws_secret_access_key)


def invoke_function(payload):
    return client.invoke(FunctionName=conf.lambda_function_name,
                         InvocationType='RequestResponse',
                         Payload=json.dumps(payload))
