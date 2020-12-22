import stream
import threading
from stock_feed1 import StockFeed
import boto3
from boto3.dynamodb.conditions import Key, Attr
from Streamio.setup_stream import Streamio
from datetime import datetime





class PagesFeed():
	def __init__(self):
		self.primary_dict={}
		self.hashtagslist=[]
		# pass

# {
# 	"Amazon":{
# 		"username":"",
# 		"image":"",
# 		"search":""
# 	}	
# }


	def get_profile_image(self):
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('database-dev')
		response = table.query(
		    KeyConditionExpression=Key('hk').eq('stocks')
		)
		stocks_value=response['Items']
		for values in stocks_value:
				self.primary_dict[values['username']]={"username":values['username'],"image":values['image'],"search":values['sk']}
				self.hashtagslist.append(values['username'])
		
		# print(self.primary_dict)

	def insert_items(self):
		now = datetime.now()
		dt_string = now.strftime("%H-%M-%S")
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('hashtagstable')
		table.put_item(Item={
			"hashtags":"hashtags",
			"datetimestamp":str(dt_string),
			"hashtagslist":self.hashtagslist
			})
	def get_feed(self):
		
		# stocks={'Amazon':'AMZN','Apple':'AAPL','Google':'GOOGL'}
		for key, value in self.primary_dict.items():
			self.adding_the_feed_stocks(value['username'],value['image'],value['search'])

		return "feed is sucessfull"

	def adding_the_feed_stocks(self,username,image,search):
			now = datetime.now()
			dt_string = now.strftime("%d,%m,%Y,%H,%M,%S")
			feedlist=StockFeed(company_name=username,profile_image=image)
			r=feedlist.searchfinhubstocknews(search)

			client=Streamio()
			self.client=client._connect()
	# 		#user name will be in small form
			feed = self.client.feed('pages', username.lower().replace(" ",""))
			itera=0
			for key1, value1 in r.items():
				feed.add_activity({
				  "actor": username.lower().replace(" ",""),
				  "verb": "post",
				  "object": value1,
				  "to":["hashtags:"+username.lower().replace(" ","")],
				  "time": str(datetime.now())
				})
				itera=itera+1
				#how much feed you want to insert
				if(itera>=2):
					break



x=PagesFeed()
x.get_profile_image()
x.insert_items()
y=x.get_feed()
print(y)
# x.adding_the_feed_stocks()