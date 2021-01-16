import stream
from Streamio.setup_stream import Streamio
import json
from datetime import date, datetime
class Get_pages_feed():
	def __init__(self,pagename,userid,limit,offset):
		self.pagename = pagename
		self.temp_dict = {}
		self.temp_list = []
		self.userid = userid
		self.limit = int(limit)
		self.offset = int(offset)


	def get_pagesfeed(self):
		client = Streamio()
		self.client = client._connect()
		feed = self.client.feed('pages',self.pagename) 
		activities = feed.get(limit=self.limit, offset=self.offset,reactions={"counts": True,"own": True})
		# print(activities,"activities")
		for item,check_like in enumerate(activities["results"]):

		# 	print(activities["results"][item]["time"])
			self.temp_dict = json.loads(activities["results"][item]["object"])
			self.temp_dict["id"] = check_like["id"]
			self.temp_dict["actor"] = check_like["actor"]
			self.temp_dict["time"] = str(check_like["time"])
			# self.temp_dict["to"] = check_like["to"]
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
		# 	# print(activities["results"][0])
		
		# print(self.temp_list)
		return self.temp_list

		# return json.dumps(activities,default=self.json_serial)

# x=Get_pages_feed(pagename="google",userid="1234userid",limit="2",offset="0")
# y=x.get_pagesfeed()
# print(y)