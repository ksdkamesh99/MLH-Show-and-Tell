import boto3
import json


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table('Students')

def lambda_handler(event, context):
    unique_id=str(event["queryStringParameters"]["id"])
    firstname=str(event["queryStringParameters"]["fname"])
    lastname=str(event["queryStringParameters"]["lname"])
    techstack=str(event["queryStringParameters"]["techstack"])
    item={}
    item["id"]=unique_id
    item["firstname"]=firstname
    item["lastname"]=lastname
    item["techstack"]=techstack
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps('Data Stored Successfully')
    }
    
    
