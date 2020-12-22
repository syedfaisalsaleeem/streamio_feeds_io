import json
import stream
from Streamio.setup_stream import Streamio
import boto3
from boto3.dynamodb.conditions import Key, Attr

class Get_likes_user():
	def __init__(self,activity_id):
		self.activity_id=activity_id

	def get_all_likes_user(self):
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('database-dev')
		activity_id=self.activity_id
		client=Streamio()
		self.client=client._connect()
		reactions = self.client.reactions.filter(
		    activity_id=activity_id,
		    kind='like')
		object_return={}
		capture_results=reactions['results']
		for values in capture_results:
			response = table.query(
		    KeyConditionExpression=Key('hk').eq(values['user_id'])
			)

			object_return[values['user_id']]=response['Items']

		return object_return

# x=Get_likes_user(activity_id="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.get_all_likes_user()
# print(y)
