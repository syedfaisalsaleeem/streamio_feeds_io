import boto3
from boto3.dynamodb.conditions import Key, Attr
class Getusers_profile():
	def __init__(self,userid):
		self.userid=userid

	def get_profile(self):
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('database-dev')
		response = table.query(
		KeyConditionExpression=Key('hk').eq(str(self.userid))
		)
		# print(response)
		return response['Items']

# x=Getusers_profile(userid="1234userid")
# y=x.get_profile()
# print(y)