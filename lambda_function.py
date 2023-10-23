import boto3
import os
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    try:
        response = table.query(
            ProjectionExpression='TeamId,#n',
            KeyConditionExpression=Key('PK').eq('Team'),
            ExpressionAttributeNames = {'#n': 'Name'}
        )
        return {'statusCode': 200, 'body':json_util.loads(response['Items'])}
    except Exception as e:
        print(e)
    finally:
        print('## ENVIRONMENT VARIABLES')
        print(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
        print(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
        print(os.environ['TABLE_NAME'])
        print('## EVENT')
        print(event)