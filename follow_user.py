import stream
from Streamio.setup_stream import Streamio
class followUser():
	def __init__(self,userid,followuserid):
		self.userid=userid
		self.followuserid=followuserid

	def followusers(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('timeline', self.userid)
		feed.follow("user",self.followuserid)
		return "user is followed"