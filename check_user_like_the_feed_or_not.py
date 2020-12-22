import stream
from Streamio.setup_stream import Streamio
class checkFeed():
	def __init__(self,userid,activity_id):
		self.userid=userid
		self.activityid=activity_id

	def checkingfeed(self):
		client=Streamio()
		self.client=client._connect()
		reactions = self.client.reactions.filter(
		    activity_id=self.activityid,
		    kind='like',
		    user_id=self.userid
		)
		# print(reactions)
		# print(len(reactions['results']))
		if(len(reactions['results'])>=1):
			return "True"
		else:
			return "False"
		# return reactions

# x=checkFeed(userid="1234userid",activity_id="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.checkingfeed()
# print(y)

		