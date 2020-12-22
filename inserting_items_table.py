import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html

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
def insert_items():
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('hashtagstable')
	table.put_item(Item={
		"hashtags":"hashtags",
		"datetimestamp":str(dt_string),
		"hashtagslist":["trending3","apple1",'orange2','tiingo','amazon','nine','undertaker']
		})

# # The BatchWriteItem API allows us to write multiple items to a table in one request.
# with table.batch_writer() as batch:
#     batch.put_item(Item={"Author": "John Grisham", "Title": "The Rainmaker",
#         "Category": "Suspense", "Formats": { "Hardcover": "J4SUKVGU", "Paperback": "D7YF4FCX" } })
#     batch.put_item(Item={"Author": "John Grisham", "Title": "The Firm",
# insert_items()
def get_items():
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('hashtagstable')
	print(dt_string,lasthour)
	resp = table.query(
    TableName='hashtagstable',
	KeyConditionExpression=Key('hashtags').eq('hashtags') & Key('datetimestamp').gt(lasthour),

    # KeyConditionExpression=Key('hashtags').eq(str("hashtags")),
    # # KeyConditionExpression="hashtags = hashtags ",
    # # ExpressionAttributeValues={
    # #     ":pk": { "S": "GAME#{}".format(game_id) },
    # #     ":metadata": { "S": "#METADATA#{}".format(game_id) },
    # #     ":users": { "S": "USER$" },
    # # },
    ScanIndexForward=True
	)
	# print(resp['Items'])
	return resp['Items']


def count_hashtags(items):
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
			if(max_hashtag_list>2):
				if(len(return_hashtag_list)<=2):
					return_hashtag_list.append(key)
				else:	
					return return_hashtag_list
			else:
				return list(re1)





insert_items()
# x=get_items()
# y=count_hashtags(x)
# print(y)
