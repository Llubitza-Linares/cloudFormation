import json
import boto3
import os

database = os.environ["MY_DATABASE"]

def getUser(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps({
        "database": database,
    }))
    return {
        'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
    }
    
def putUser(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps({
        "database": database,
    }))
    return {
        'statusCode': 200,
      'body': json.dumps('Hello from Lambda!')
    }