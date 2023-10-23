import boto3
import os
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ['TABLE_NAME'])
        response = table.query(
            ProjectionExpression='TeamId,#n',
            KeyConditionExpression=Key('PK').eq('Team'),
            ExpressionAttributeNames = {'#n': 'Name'}
        )
        # return {
        #     'statusCode': 200,
        #     'body':json_util.dumps(response['Items'])
        # }
        return {
            'statusCode': 200, 
            'body': json_util.dumps(response['Items'])
        }
    except Exception as e:
        print(f'Exception: {e}')

    return {
            'statusCode': 500,
            'body': json_util.dumps('Invalid Request')
        }