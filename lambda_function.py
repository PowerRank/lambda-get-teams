import boto3
import os
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util

def lambda_handler(event, context):
    try:
        print("Executing Get Teams")

        print("Connecting to DynamoDb...")
        dynamodb = boto3.resource('dynamodb')

        print("Connecting to Table..")
        table = dynamodb.Table(os.environ['TABLE_NAME'])

        print("Running teams query...")
        response = table.query(
            ProjectionExpression='TeamId,#n',
            KeyConditionExpression=Key('PK').eq('Team'),
            ExpressionAttributeNames = {'#n': 'Name'}
        )

        print("Returning response...")
        print(json_util.dumps(response['Items']))
        return {
            'statusCode': 200,
            'body': json_util.dumps(response['Items'])
        }
        # return {'statusCode': 200, 'body':json_util.loads(response['Items'])}
    except Exception as e:
        print("Exception Found...")
        print(e)
    finally:
        print('## ENVIRONMENT VARIABLES')
        print(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
        print(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
        print(os.environ['TABLE_NAME'])
        print('## EVENT')
        print(event)
    return {
            'statusCode': 200,
            'body': json_util.dumps('Invalid Request')
        }