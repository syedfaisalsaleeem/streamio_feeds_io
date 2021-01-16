import stream
from Streamio.setup_stream import Streamio
class Likefeed():
	def __init__(self,userid,activityid):
		self.userid = userid
		self.activityid = activityid

	def likingfeed(self):
		client=Streamio()
		self.client=client._connect()
		# feed = self.client.feed('pages',self.pagename)
		reactions = self.client.reactions.filter(
		activity_id=self.activityid,
		kind='like')
		# print("reaction",reactions["results"])
		x = 0
		self.capturereation = False
		for checkreaction in reactions["results"]:
			if(x==0):
				if(checkreaction["user_id"]==self.userid ):
					self.capturereation = True
					self.captureid = checkreaction["id"]
					x = 1
				else:
					self.capturereation = False
				# print("true")

		if(self.capturereation==True):
			self.client.reactions.delete(self.captureid)
			return "successfully unliked the feed"

		else:
			self.client.reactions.add("like", self.activityid, user_id=self.userid)
			return "successfully liked the feed"


		# result = feed.get(offset=0, limit=1, id_lt=last_activity.id)
		# feed->getActivities(offset=0, limit=1, ['id_gte' => $id]);
		# 'b7bcd2a2-363e-11eb-8080-800160b53eae'
		# self.client.reactions.add("like", self.activityid, user_id=self.userid)
		# return "successfully liked the feed"


# x=Likefeed(userid="seconduserid",activityid='b85613f4-363e-11eb-8080-80000b6503b3')
# y=x.likingfeed()
# print(y)