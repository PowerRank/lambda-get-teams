import boto3
import os
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.query(
        ProjectionExpression='TeamId,#n',
        KeyConditionExpression=Key('PK').eq('Team'),
        ExpressionAttributeNames = {'#n': 'Name'}
    )
    return {'statusCode': 200, 'body':json_util.loads(response['Items'])}