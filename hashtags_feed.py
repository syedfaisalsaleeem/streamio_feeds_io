import stream
from Streamio.setup_stream import Streamio
import json
class Get_hashtags_Feed():
	def __init__(self,hashtag):
		self.hashtag=hashtag


	def gethashtags_feed(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('hashtags', self.hashtag)
		activities = feed.get()
		# print(activities)
		return json.dumps(activities, indent=4, sort_keys=True, default=str)

# x=Get_hashtags_Feed(hashtag="google")
# y=x.gethashtags_feed()
# print(y)