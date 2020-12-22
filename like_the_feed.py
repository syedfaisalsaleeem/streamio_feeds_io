import stream
from Streamio.setup_stream import Streamio
class Likefeed():
	def __init__(self,userid,activityid):
		self.userid=userid
		self.activityid=activityid

	def likingfeed(self):
		client=Streamio()
		self.client=client._connect()
		self.client.reactions.add("like", self.activityid, user_id=self.userid)
		return "successfully liked the feed"


# x=Likefeed(userid="1234userid",activityid="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.likingfeed()
# print(y)