import boto3
import json
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
    teams = response['Items']
    for team in teams:
        team['TeamId']=int(team['TeamId'])
    return {'statusCode': 200, 'body':json.dumps(json_util.loads(response['Items']))}