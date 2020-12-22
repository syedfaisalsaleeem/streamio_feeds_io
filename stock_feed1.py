import requests
import twitter
import json
import praw
from datetime import date
from creating_token import token

#object for feed
		# object={
		#     "profile_picture":self.profile_picture,
		#     "category":self.username,
		#     "datetime":dt_string,
		#     "headline":"null",
		# 	"image":self.storedimage,
		# 	"summary":str(self.summary),
		# 	"url":str(self.url),
		# 	"hashtags":self.hashtag,
		# 	"likes":"0",
		# 	"no_of_comments":"0"
		# }

# print(token.finhub_token)
class StockFeed:
	def __init__(self,company_name=None,profile_image=None):
		self.company_name=company_name
		self.profile_image=profile_image
		self.main_dict={}

	def searchfinhub(self):
		try:
			sup_dict={}
			r=requests.get('https://finnhub.io/api/v1/news?category=general&token='+token.finhub_token)
			y=r.json()
			for t in y:
				self.main_dict[str(t["id"])]={
				"id":t["id"],
				"category":t["category"],
				"datetime":t["datetime"],"image":t["image"],
				"summary":t["summary"],
				"url":t["url"],
				"headline":t["headline"]}
				# print(self.main_dict)
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
			return self.main_dict
		except:
			return {}
			print("error")
	def searchfinhubstocknews(self,symbol):
		try:
			today = date.today()
			# print(type(today))
			d2 = today.strftime("%Y")
			d1 = today.strftime("-%m-%d")
			lastyear=str(int(d2)-1)+d1
			sup_dict={}
			# print(lastyear,today)
			r = requests.get('https://finnhub.io/api/v1/company-news?symbol='+symbol+'&from='+lastyear+'&to='+str(today)+'&token='+token.finhub_token)
			y=r.json()

		# object={
		#     "profile_picture":self.profile_picture,
		#     "category":self.username,
		#     "datetime":dt_string,
		#     "headline":"null",
		# 	"image":self.storedimage,
		# 	"summary":str(self.summary),
		# 	"url":str(self.url),
		# 	"hashtags":self.hashtag,
		# 	"likes":"0",
		# 	"no_of_comments":"0"
		# }

			for t in y:
				self.main_dict[str(t["id"])]={
				"profile_picture":self.profile_image,
				"category":self.company_name,
				"datetime":t["datetime"],
				"image":t["image"],
				"summary":t["summary"],
				"url":t["url"],
				"headline":t["headline"],
				"hashtags":"none",
				"likes":"0",
				"no_of_comments":"0"
				}
			# print(self.main_dict)
			return self.main_dict
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
		except:
			return {}
			print("error")
	def searchtwitter(self,tags1):
		try:
			main_dict=[]
			sup_dict={}
			# print("here")
			print(			token.consumer_key_twitter,
	        token.consumer_secret_twitter,
	        token.access_token_key_twitter,
	        token.access_token_secret_twitter)

			api = twitter.Api(consumer_key=token.consumer_key_twitter,
	                  consumer_secret=token.consumer_secret_twitter,
	                  access_token_key=token.access_token_key_twitter,
	                  access_token_secret=token.access_token_secret_twitter)
			print(api.tweet_mode)
			# print(api.tweet_mode,"worked")
			results = api.GetSearch(
			    raw_query="q="+tags1)
			# y=results[0].AsDict()
			# print(y)
			try:
				
				for x,t in enumerate(results):
					y=results[x].AsDict()
					try:
						if('media'in y) and (len(y["urls"])!=0):
							# print(y['media'][0]['media_url'])
							# print("media")
							if(y["lang"]=="en"):
								# print("worked1",main_dict)
								self.main_dict[str(y["id"])]={
								"id":y["id"],
								"category":tags1,"datetime":y["created_at"],
								"image":y['media'][0]['media_url'],
								"summary":y["text"],
								"url":y["urls"][0]["expanded_url"],
								"headline":y["source"]}
								continue
								
						elif('media'in y):
							# print(y['media'][0]['media_url'])
							if(y["lang"]=="en"):
								# print("worked2",main_dict)
								self.main_dict[str(y["id"])]={
								"id":y["id"],
								"category":tags1,"datetime":y["created_at"],
								"image":y['media'][0]['media_url'],
								"summary":y["text"],
								"url":"null",
								"headline":y["source"]}
								continue
						elif(len(y["urls"])!=0):
							# print(y["lang"],y["urls"])
							if(y["lang"]=="en"):
								# print("worked3",main_dict)
								self.main_dict[str(y["id"])]={
								"id":y["id"],
								"category":tags1,"datetime":y["created_at"],"image":"null",
								"summary":y["text"],
								"url":y["urls"][0]["expanded_url"],
								"headline":y["source"]}
								continue
						else:
							continue
							# print("none1")
					except:
						return {}
						# print("none")


			except:
				return {}
				# print("")
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
			return self.main_dict
		except Exception as e:
			print(e)
			return {}
			

			# print(t["category"],"1")
	def searchstockwits(self,sector):
		# print(token.stockwits_token)
		try:
			headers = {
			'Content-Type': 'application/json'
			}
			token1=requests.get("https://api.stocktwits.com/api/2/streams/trending.json?access_token="+token.stockwits_token,headers)
			# print(token1._content)
			y=json.loads(token1._content)
			# print(y['messages'])
			# sup_dict={}
			# r=requests.get('https://finnhub.io/api/v1/news?category=general&token=bufvijf48v6qf6lbs26g')
			# y=r.json()
			for t in y['messages']:
				# print(t)
				self.main_dict[str(t["id"])]={"id":t["id"],
				"category":sector,
				"datetime":t["created_at"],
				"image":"null",
				"summary":t["body"],
				"url":t['source']["url"],
				"headline":t['source']["title"]}
			return self.main_dict
			# stock_feed_list=[]
			# stock_feed_list.append(self.main_dict)	
			# print(stock_feed_list)
		except:
			return self.main_dict
			# print("error")
	def searchtiingo(self,typeof,sector):
		try:
			# For the latest news
			if(typeof=="trending"):
				headers = {
				'Content-Type': 'application/json'
				}
				token1=requests.get("https://api.tiingo.com/tiingo/news?&token="+token.tiingo_token, headers=headers)
				y=token1.json()
				for t in y:
					# print(t)
					self.main_dict[str(t["id"])]={"id":t["id"],
					"category":sector,
					"datetime":t["publishedDate"],
					"image":"null",
					"summary":t["description"],
					"url":t["url"],
					"headline":t["title"]}
				return self.main_dict
				# stock_feed_list=[]
				# stock_feed_list.append(self.main_dict)	
				# print(stock_feed_list)
			elif(typeof=="sector"):
				headers = {
				'Content-Type': 'application/json'
				}
				token1=requests.get("https://api.tiingo.com/tiingo/news?tags="+sector+"&token="+token.tiingo_token, headers=headers)
				y=token1.json()
				for t in y:
					# print(t)
					self.main_dict[str(t["id"])]={"id":t["id"],
					"category":sector,
					"datetime":t["publishedDate"],
					"image":"null",
					"summary":t["description"],
					"url":t["url"],
					"headline":t["title"]}
				return self.main_dict
				# stock_feed_list=[]
				# stock_feed_list.append(self.main_dict)	
				# print(stock_feed_list)		
			elif(typeof=="stocks"):
				headers = {
				'Content-Type': 'application/json'
				}
				token1=requests.get("https://api.tiingo.com/tiingo/news?tickers="+sector+"&token="+token.tiingo_token, headers=headers)
				y=token1.json()
				for t in y:
					# print(t)
					self.main_dict[str(t["id"])]={"id":t["id"],
					"category":sector,
					"datetime":t["publishedDate"],
					"image":"null",
					"summary":t["description"],
					"url":t["url"],
					"headline":t["title"]}
				return self.main_dict
				# stock_feed_list=[]
				# stock_feed_list.append(self.main_dict)	
				# print(stock_feed_list)	
		except:
			return self.main_dict
			# print("error")
	def searchreddit(self,sector):
		try:
			client_id=token.reddit_client_id
			client_secret=token.reddit_client_secret
			user_agent=token.reddit_user_agent
			reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,password=token.reddit_password,username=token.reddit_username,user_agent=user_agent)
			hot_posts = reddit.subreddit("all").search(sector,limit=100)
			temp_dict={}
			temp_attributes={}
			for post in hot_posts:
				if("self" in post.thumbnail or "spoiler" in post.thumbnail or "default" in post.thumbnail):
					image="null"
				else:
					image=post.thumbnail
				self.main_dict[str(post.id)]={"id":post.id,
				"category":sector,
				"datetime":post.created,
				"image":image,
				"summary":post.selftext,
				"url":post.url,
				"headline":post.title}
			return self.main_dict
		except:
			return self.main_dict



##there maybe many different feeds with same id because user follows it we have to get unique only when i will be making an object and putting
## it in user feed i have to make the feed unique with id
# tags={'stocks':['AMZN','AAPL'],'sector':['trending','industrials','materials','financials','Energy','Consumer Discretionary','Information technology','Communication services','Real estate','Health care','Consumer Staples','utilites']}
# feedlist=StockFeed(tags['sector'])
# # feedlist.searchfinhubstocknews(tags['stocks'][0])
# feedlist.searchfinhub()
# # feedlist.searchstockwits(tags['sector'][0])
# # feedlist.searchtiingo('stocks',tags['stocks'][0])
# feedlist.searchreddit(tags['stocks'][0])