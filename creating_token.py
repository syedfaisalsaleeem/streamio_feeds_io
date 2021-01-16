class token:
	
	from dotenv import load_dotenv
	load_dotenv()
	import os

	finhub_token = os.getenv("clientid")
	consumer_key_twitter = os.getenv("secretid")
	finhub_token=os.getenv("finhub_token")
	consumer_key_twitter=os.getenv("consumer_key_twitter")
	consumer_secret_twitter=os.getenv("consumer_secret_twitter")
	access_token_key_twitter=os.getenv("access_token_key_twitter")
	access_token_secret_twitter=os.getenv("access_token_secret_twitter")
	stockwits_token=os.getenv("stockwits_token")
	tiingo_token=os.getenv("tiingo_token")
	reddit_client_id=os.getenv("reddit_client_id")
	reddit_client_secret=os.getenv("reddit_client_secret")
	reddit_user_agent=os.getenv("reddit_user_agent")
	reddit_password=os.getenv("reddit_password")
	reddit_username=os.getenv("reddit_username")

