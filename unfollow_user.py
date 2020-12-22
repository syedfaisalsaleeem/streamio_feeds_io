import stream
from Streamio.setup_stream import Streamio
class UnfollowUser():
	def __init__(self,userid,followuserid):
		self.userid=userid
		self.followuserid=followuserid

	def unfollowusers(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('timeline', self.userid)
		feed.unfollow("user",self.followuserid)
		return "user is unfollowed"