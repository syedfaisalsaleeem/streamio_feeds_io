import json
import stream
from Streamio.setup_stream import Streamio
import boto3
from boto3.dynamodb.conditions import Key, Attr

class Commentfeed():
	def __init__(self,userid,activityid,text):
		self.text=text
		self.userid=userid
		self.activityid=activityid
		self.temp_dict = {}
	def commentingfeed(self):
		client=Streamio()
		self.client=client._connect()
		x=self.client.reactions.add("comment", self.activityid, user_id=self.userid,data={"text": self.text})
		self.temp_dict = x
		self.temp_dict["message"] = "successfully commented the feed"
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('database-dev')
		response = table.query(
		KeyConditionExpression=Key('hk').eq(x["user_id"])
		)
		self.temp_dict['user_details'] = response["Items"][0]
		return self.temp_dict
		# print(x)
		# self.client.reactions.add("like", self.activityid, user_id=self.userid)
		# return "successfully commented the feed"


# x=Commentfeed(userid="1234userid",activityid="77dc977e-3618-11eb-8080-80001ae9b3e2",text="this is post comment")
# y=x.commentingfeed()
# print(y)