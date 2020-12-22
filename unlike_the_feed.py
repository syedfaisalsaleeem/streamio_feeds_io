import stream
from Streamio.setup_stream import Streamio
class UnLikefeed():
	def __init__(self,reactionid):
		self.reactionid=reactionid

	def unlikingfeed(self):
		client=Streamio()
		self.client=client._connect()
		self.client.reactions.delete(self.reactionid)
		return "successfully unliked the feed"


# x=UnLikefeed(reactionid="be33c384-2280-407c-b495-75388617dbb5")
# y=x.unlikingfeed()
# print(y)