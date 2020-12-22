import stream
from Streamio.setup_stream import Streamio
class UnfollowPage():
	def __init__(self,userid,pagename):
		self.userid=userid
		self.pagename=pagename

	def unfollowpages(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('timeline', self.userid)
		feed.unfollow("pages",self.pagename)
		return "page is unfollowed"


# x=UnfollowPage(userid="1234userid",pagename="google")
# y=x.unfollowpages()
# print(y)


