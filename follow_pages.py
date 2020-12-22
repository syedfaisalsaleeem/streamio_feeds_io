import stream
from Streamio.setup_stream import Streamio

class Followpage():
	def __init__(self,userid=None,follow_list=None):
		self.userid=userid
		self.follow_list=follow_list

	def follow_the_page(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('timeline', self.userid)
		for x in self.follow_list:
			feed.follow("pages", x.lower().replace(" ",""),activity_copy_limit=500)

		return "users are followed"

# x=Followpage(userid="1234userid",follow_list=['google'])
# y=x.follow_the_page()
# print(y)