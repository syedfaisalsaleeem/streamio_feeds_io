import stream
from Streamio.setup_stream import Streamio
class Commentfeed():
	def __init__(self,userid,activityid,text):
		self.text=text
		self.userid=userid
		self.activityid=activityid

	def commentingfeed(self):
		client=Streamio()
		self.client=client._connect()
		self.client.reactions.add("comment", self.activityid, user_id=self.userid,data={"text": self.text})
		self.client.reactions.add("like", self.activityid, user_id=self.userid)
		return "successfully commented the feed"


# x=Commentfeed(userid="1234userid",activityid="77dc977e-3618-11eb-8080-80001ae9b3e2",text="this is post comment")
# y=x.commentingfeed()
# print(y)