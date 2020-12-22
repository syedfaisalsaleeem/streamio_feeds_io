import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('database-dev')
# print(table)
# response=table.put_item(Item={"hk": "1234userid", "sk": "+923312812064",
# "sk2": "demo","image":"https://avatars2.githubusercontent.com/u/49129677?s=460&u=799c8f88886ed9f191f0f9863e2b86b9b0735881&v=4","username":"syed faisal"})
# print(response)
# resp = table.get_item(Key={"hk": "+923312812064", "sk": "1234userid"})
# print(resp['Item'])
response = table.query(
    KeyConditionExpression=Key('hk').eq('stocks')
)
print(response['Items'])
# print(response['Items'][0]['username'])
# print(response['Items'][0]['image'])