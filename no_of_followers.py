import stream
from Streamio.setup_stream import Streamio

class No_followers():
	def __init__(self,userid):
		self.userid=userid
		# pass

	def return_no_of_followers(self):
		temp_list={}
		client=Streamio()
		self.client=client._connect()
		feed1 =self.client.feed('timeline', self.userid)
		a=feed1.following(limit=100)
		temp_list['followers']=a['results']
		temp_list['no_of_followers']=len(a['results'])
		# print(temp_list)
		return temp_list


		# userid=event['params']['querystring']['user']
		# client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
		# feed1 = client.feed('user', userid)
		# a=feed1.following(limit=100)
		# temp_list['followers']=a['results']
		# temp_list['no_of_followers']=len(a['results'])

# x=No_followers(userid="1234userid")
# y=x.return_no_of_followers()
# print(y)

