import stream
from Streamio.setup_stream import Streamio
import json
from datetime import date, datetime
class Get_pages_feed():
	def __init__(self,pagename):
		self.pagename=pagename


	def json_serial(self,obj):
	    """JSON serializer for objects not serializable by default json code"""

	    if isinstance(obj, (datetime, date)):
	        return obj.isoformat()
	    raise TypeError ("Type %s not serializable" % type(obj))
	def get_pagesfeed(self):
		client=Streamio()
		self.client=client._connect()
		feed = self.client.feed('pages',self.pagename)
		activities = feed.get(reactions={"counts": True})
		# print(activities)
		return json.dumps(activities,default=self.json_serial)

# x=Get_pages_feed(pagename="google")
# y=x.get_pagesfeed()
# print(y)