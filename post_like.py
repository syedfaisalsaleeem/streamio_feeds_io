import stream
from Streamio.setup_stream import Streamio
class Postlike():
	def __init__(self,user_id,activity_id):
		self.user_id=user_id
		self.activity_id=activity_id
		client=Streamio()
		self.client=client._connect()
	def add_like(self):
		try:
			self.client.reactions.add("like", self.activity_id, user_id=self.user_id)
			return "like true"
		except:
			return "like false"
	def get_no_like(self):
		# try:
			reactions = self.client.reactions.filter(
			    activity_id=self.activity_id,
			    kind='like',
			)
			return len(reactions['results'])
		# except:
		# 	return "error"
	def get_reactions(self):
		try:
			reactions = self.client.reactions.filter(activity_id=self.activity_id)
			return reactions
		except:
			return "error"
	def get_no_comments(self):
		try:
			reactions = self.client.reactions.filter(activity_id=self.activity_id,kind='comment')
			return len(reactions['results'])
		except:
			return "error"
	# def post_like(self):

	# 	# client.reactions.add("like", activity_id, user_id=user_id)
# user_id="ac211c30-ffdd-40af-9402-d3b36a671a7b"
# activity_id="5f09e455-1fa0-11eb-bec3-128a130028af"
# x=Postlike(user_id,activity_id)
# y=x.get_no_like()
# print(y)