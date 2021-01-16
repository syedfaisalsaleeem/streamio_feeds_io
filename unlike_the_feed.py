import stream
from Streamio.setup_stream import Streamio
class UnLikefeed():
	def __init__(self,reactionid):
		self.reactionid = reactionid

	def unlikingfeed(self):
		client=Streamio()
		self.client=client._connect()
		self.client.reactions.delete(self.reactionid)
		return "successfully unliked the feed"


# for x1 in ['5d8fb629-8fac-45cb-9021-b53c61008850','80642060-12b1-451e-bb6a-5bebda947b3d','9230c177-3850-4d52-a238-e5c2054d249b','68dc82d2-424e-4c4b-ae1f-31aab6d3fa1e']:
# 	x=UnLikefeed(reactionid=x1)
# 	y=x.unlikingfeed()
# 	print(y)


