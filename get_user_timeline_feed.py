import stream
from Streamio.setup_stream import Streamio
# from bson import json_util
import json
class Get_user_time_feed():
	def __init__(self,userid,limit,offset):
		self.temp_dict = {}
		self.temp_list = []
		self.userid = userid
		self.limit = int(limit)
		self.offset = int(offset)

	def get_user_timelinesfeed(self):
		# client=Streamio()
		# self.client=client._connect()
		# feed = self.client.feed('timeline', self.userid)
		# activities = feed.get(reactions={"counts": True})
		# # print(activities)
		# return json.dumps(activities, indent=4, sort_keys=True, default=str)

		client = Streamio()
		self.client = client._connect()
		feed = self.client.feed('timeline', self.userid) 
		activities = feed.get(limit=self.limit, offset=self.offset,reactions={"counts": True,"own": True})

		for item,check_like in enumerate(activities["results"]):

			self.temp_dict = json.loads(activities["results"][item]["object"])
			self.temp_dict["id"] = check_like["id"]
			self.temp_dict["actor"] = check_like["actor"]
			self.temp_dict["time"] = str(check_like["time"])
			self.temp_dict["current_user_like"] =  False

			if "like" in check_like["reaction_counts"].keys():
				self.temp_dict["likes"] = check_like["reaction_counts"]["like"]
			else:
				self.temp_dict["likes"] = 0
			if "comments" in check_like["reaction_counts"].keys():
				self.temp_dict["no_of_comments"] = check_like["reaction_counts"]["like"]
			else:
				self.temp_dict["no_of_comments"] = 0
			if("like" in check_like['own_reactions'].keys()):
				for check_like_true in check_like['own_reactions']['like']:
					if(check_like_true['user_id']==self.userid):
						self.temp_dict["current_user_like"] =  True

			self.temp_list.append(self.temp_dict)
		return self.temp_list



# x=Get_user_time_feed(userid="1234userid",limit="2",offset="2")
# y=x.get_user_timelinesfeed()
# print(y)
# json.dumps(anObject, default=json_util.default)