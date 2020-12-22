import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
class trendinghashtags():
	def __init__(self,limit=10):
		self.limit=int(limit)

	def get_items(self):
		now = datetime.now()
		dt_string = now.strftime("%H-%M-%S")
		h2 = now.strftime("%H")
		h1 = now.strftime("-%M-%S")
		if(int(h2)<=9):
			lasthour=str(int(h2)-1)+h1
			lasthour="0"+lasthour
		else:
			lasthour=str(int(h2)-1)+h1
		print(dt_string)
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('hashtagstable')
		print(dt_string,lasthour)
		resp = table.query(
	    TableName='hashtagstable',
		KeyConditionExpression=Key('hashtags').eq('hashtags') & Key('datetimestamp').gt(lasthour),
	    ScanIndexForward=True
		)
		if(len(resp['Items'])==0):
			dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
			table = dynamodb.Table('hashtagstable')
			print(dt_string,lasthour)
			resp = table.query(
		    TableName='hashtagstable',
			KeyConditionExpression=Key('hashtags').eq('hashtags'),
		    ScanIndexForward=True
			)
			return resp['Items']
		else:
			return resp['Items']


	def count_hashtags(self,items):
		t=[]
		counts={}
		return_hashtag_list=[]
		max_hashtag_list=0
		if(len(items)>0):
			# print(items[])
			for values in items:
				t=t+values['hashtagslist']
				# print(values['hashtagslist']))
			# print(t)
			# t.sort()
			for words in t:
				counts[words]=counts.get(words,0)+1
			# print(counts)

			re1=dict(sorted(counts.items(), key=lambda item: item[1],reverse=True))
			max_hashtag_list=len(list(re1))
			print(re1)
			# print(list(re1))
			index=0
			for key,value in re1.items():
				if(self.limit>max_hashtag_list):
					return list(re1)

				else:
					if(max_hashtag_list>8):
						if(len(return_hashtag_list)<=self.limit):
							return_hashtag_list.append(key)
						else:	
							return return_hashtag_list
					else:
						return list(re1)





# insert_items()
# hashtags=trendinghashtags(limit="4")
# items=hashtags.get_items()
# return_hashtag_list=hashtags.count_hashtags(items)
# print(return_hashtag_list,"this is return")