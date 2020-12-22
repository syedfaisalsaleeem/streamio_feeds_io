import json
import stream
from Streamio.setup_stream import Streamio
import boto3
from boto3.dynamodb.conditions import Key, Attr

class Get_comments_user():
	def __init__(self,activity_id):
		self.activity_id=activity_id
		self.temp_dict = {}
		self.temp_list = []
		self.return_dict = {}
	def get_all_comments_user(self):
		activity_id = self.activity_id
		client = Streamio()
		self.client = client._connect()
		reactions = self.client.reactions.filter(
		    activity_id = activity_id,
		    kind='comment')
		# print(reactions['results'])

		for value in reactions['results']:
			# print(value)

			dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
			table = dynamodb.Table('database-dev')
			response = table.query(
			KeyConditionExpression=Key('hk').eq(value["user_id"])
			)
			# print(response['Items'])
			self.temp_dict = value
			self.temp_dict['user_details'] = response["Items"][0]
			self.temp_list.append(self.temp_dict)
		
		# print(self.temp_dict)
		self.return_dict["results"] = self.temp_list
		return self.return_dict
		# return response['Items']
		# return reactions
# https://9q2d566izk.execute-api.us-east-1.amazonaws.com/dev/commentsfeed?activityid=bd3b9da6-33cc-11eb-a511-0a1200300037

# x = Get_comments_user(activity_id="bd3b9da6-33cc-11eb-a511-0a1200300037")
# y = x.get_all_comments_user()
# print(y)