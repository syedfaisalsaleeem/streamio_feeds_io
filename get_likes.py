import json
import stream
from Streamio.setup_stream import Streamio
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('database-dev')
# user_id="ac211c30-ffdd-40af-9402-d3b36a671a7b"
# activity_id="5f09e455-1fa0-11eb-bec3-128a130028af"
# client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
# reactions = client.reactions.filter(
#     activity_id=activity_id,
#     kind='like',
# )
# print(len(reactions))
user_id="1234userid"
activity_id="77dc977e-3618-11eb-8080-80001ae9b3e2"
# client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
# client.reactions.add("comment", activity_id, user_id=user_id,data={"text": "awesome post!"})
client1=Streamio()
client2=client1._connect()
reactions = client2.reactions.filter(
    activity_id=activity_id,
    kind='like',
)
# feed = client2.feed('hashtag', 'trending')
# activities = feed.get(reactions={"counts": True})
object_return={}
capture_results=reactions['results']
for values in capture_results:
	# print(values['user_id'])
	response = table.query(
    KeyConditionExpression=Key('hk').eq(values['user_id'])
	)
	# print(response['Items'])
	object_return[values['user_id']]=response['Items']

print(object_return)
# capture_userid=capture_results['user_id']
# print(capture_userid)
