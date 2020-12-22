import boto3
from boto3.dynamodb.conditions import Key, Attr
class Getpages_profile():
	def __init__(self,pagename):
		self.pagename=pagename

	def get_pages(self):
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
		table = dynamodb.Table('database-dev')
		response = table.scan(
			FilterExpression=Attr('sk2').eq(self.pagename)
		)
		# print(response)
		return response['Items']

# x=Getpages_profile(pagename="google")
# y=x.get_pages()
# print(y)