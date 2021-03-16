import boto3
import json

dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table('Students')

def lambda_handler(event, context):
    unique_id=str(event['queryStringParameters']['id'])
    key={
        'id':unique_id
    }

    response_table=table.get_item(Key=key)
    
    item=response_table['Item']
    print(item)
    output_response={}
    output_response["id"]=str(item["id"])
    output_response["firstname"]=item["firstname"]
    output_response["lastname"]=item["lastname"]
    output_response["techstack"]=item["techstack"]

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(output_response)
    return responseObject
