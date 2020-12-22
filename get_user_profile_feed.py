import stream
from Streamio.setup_stream import Streamio
import json
class Getuser_profile_Feed():
	def __init__(self,userid):
		self.userid=userid


	def getuser_feed(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('user', self.userid)
		activities = feed.get()
		print(activities)
		return json.dumps(activities, indent=4, sort_keys=True, default=str)


# x=Getuser_profile_Feed(userid="1234userid")
# x.getuser_feed()
