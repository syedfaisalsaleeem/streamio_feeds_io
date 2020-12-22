import stream
from Streamio.setup_stream import Streamio
# from bson import json_util
import json
class Get_user_time_feed():
	def __init__(self,userid):
		self.userid=userid

	def get_user_timelinesfeed(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('timeline', self.userid)
		activities = feed.get(reactions={"counts": True})
		# print(activities)
		return json.dumps(activities, indent=4, sort_keys=True, default=str)



# x=Get_user_time_feed(userid="1234userid")
# y=x.get_user_timelinesfeed()
# print(y)
# json.dumps(anObject, default=json_util.default)