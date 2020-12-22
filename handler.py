import json
from flask import Flask,request,jsonify
from post_like import Postlike
from creating_feed import Creating_Feed
from socialsection.trendinghashtags import trendinghashtags
from no_of_followers import No_followers
from follow_pages import Followpage
from get_user_timeline_feed import Get_user_time_feed
from get_user_profile import Getusers_profile
from get_pages_feed import Get_pages_feed
from get_pages_profile import Getpages_profile
from get_user_profile_feed import Getuser_profile_Feed
from like_the_feed import Likefeed
from unlike_the_feed import UnLikefeed
from check_user_like_the_feed_or_not import checkFeed
from comment_the_feed import Commentfeed
from get_all_likes import Get_likes_user
from get_all_comments import Get_comments_user
from unfollow_page import UnfollowPage
from unfollow_user import UnfollowUser
from follow_user import followUser
from hashtags_feed import Get_hashtags_Feed
# from follow_user import followUser
##Two apis unfollow page,unfollowuser,follow user,gethashtagsfeed

app = Flask(__name__)


@app.route('/hello/')
def hello(event=None, context=None):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": "Hello"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

@app.route('/likes')
def likes(event=None, context=None):
    try:
        user_id="ac211c30-ffdd-40af-9402-d3b36a671a7b"
        activity_id="5f09e455-1fa0-11eb-bec3-128a130028af"
        print(event)
        x=Postlike(event['userid'],event['activityid'])
        y=x.get_no_like()
        print(y)
        body = {
            "message": "Go Serverless v1.0! Your function executed successfully!",
            "input": y,
            "input2":event
        }

        response = {
            "statusCode": 200,
            "body": body
        }

        return response
    except:
        response = {
            "statusCode": 404,
            "body": "user id or activity id not defined in query parameters"
        }

        return response


@app.route('/createpost',methods=["POST"])
def createpost(event=None, context=None):
    try:
        x=Creating_Feed(user_id=event['body']['user_id'],summary=event['body']['summary'],url=event['body']['url'],image=event['body']['image'])
    except:
        response = {
            "statusCode": 404,
            "body": "invalid parameters"
        }
        return response
    try:
        x.capturehashtag()
    except:
        response = {
            "statusCode": 400,
            "body": "error in summary"
        }
        return response
    try:
        x.insert_items()
    except:
        response = {
            "statusCode": 400,
            "body": "error in storing hashtags"
        }
        return response
    try:
        x.storingimages3()
    except:
        response = {
            "statusCode": 400,
            "body": "can't store image"
        }
        return response

    try:
        x.dynamodbquery()
    except:
        response = {
            "statusCode": 400,
            "body": "can't query dynamo db"
        }
        return response

    try:
        y=x.create()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
        # return y
    except:
        response = {
            "statusCode": 400,
            "body": "feed is not created"
        }
        return response


@app.route('/trendinghashtags')
def trendinghashtags1(event=None, context=None):
    # hashtags=trendinghashtags(limit=event['limit'])
    try:
        hashtags=trendinghashtags(limit=event['limit'])
    except:
        response = {
            "statusCode": 404,
            "body": "limit is not defined"
        }
        return response
    # items=hashtags.get_items()
    try:
        items=hashtags.get_items()
    except:
        response = {
            "statusCode": 400,
            "body": "error with dynamo db"
        }
        return response
    try:
        return_hashtag_list=hashtags.count_hashtags(items)
        response = {
            "statusCode": 200,
            "body": return_hashtag_list
        }
        return response
        # print(return_hashtag_list,"this is return")
    except:
        response = {
            "statusCode": 400,
            "body": "error in hashtags"
        }
        return response


@app.route('/followingusers')
def list_no_of_followuser(event=None, context=None):
    try:
        x=No_followers(userid=event['userid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid is not defined"
        }
        return response
    try:
        y=x.return_no_of_followers()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response


@app.route('/followpage',methods=["POST"])
def following_the_page(event=None, context=None):

    try:
        x=Followpage(userid=event['body']['userid'],follow_list=event['body']['follow_list'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid is not defined"
        }
        return response
    try:
        y=x.follow_the_page()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response



@app.route('/timelinefeed')
def list_timeline_feed(event=None, context=None):
    try:
        x=Get_user_time_feed(userid=event['userid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid is not defined"
        }
        return response
    try:
        y=x.get_user_timelinesfeed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response


# x=Getusers_profile(userid="1234userid")
# # y=x.get_profile()
# # print(y)

@app.route('/userprofile')
def get_profile_of_user(event=None, context=None):
    try:
        x=Getusers_profile(userid=event['userid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid is not defined"
        }
        return response
    try:
        y=x.get_profile()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Get_pages_feed(pagename="google")
# y=x.get_pagesfeed()
# print(y)

@app.route('/pagefeed')
def get_feed_of_page(event=None, context=None):
    try:
        x=Get_pages_feed(pagename=event['pagename'])
    except:
        response = {
            "statusCode": 404,
            "body": "pagename is not defined"
        }
        return response
    try:
        y=x.get_pagesfeed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Getpages_profile(pagename="google")
# y=x.get_pages()
# print(y)

@app.route('/pageprofile')
def get_profile_of_page(event=None, context=None):
    try:
        x=Getpages_profile(pagename=event['pagename'])
    except:
        response = {
            "statusCode": 404,
            "body": "pagename is not defined"
        }
        return response
    try:
        y=x.get_pages()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Getuser_profile_Feed(userid="1234userid")
# x.getuser_feed()
@app.route('/usersprofilefeed')
def user_profile_feed(event=None, context=None):
    try:
        x=Getuser_profile_Feed(userid=event['userid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid is not defined"
        }
        return response
    try:
        y=x.getuser_feed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Likefeed(userid="1234userid",activityid="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.likingfeed()
# print(y)
@app.route('/likefeed',methods=["POST"])
def like_the_feed(event=None, context=None):

    try:
        x=Likefeed(userid=event['body']['userid'],activityid=event['body']['activityid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or activity id is not defined"
        }
        return response
    try:
        y=x.likingfeed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response
# x=UnLikefeed(reactionid="be33c384-2280-407c-b495-75388617dbb5")
# y=x.unlikingfeed()
# print(y)
@app.route('/unlikefeed',methods=["POST"])
def unlike_the_feed(event=None, context=None):

    try:
        x=UnLikefeed(reactionid=event['body']['reactionid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or activity id is not defined"
        }
        return response
    try:
        y=x.unlikingfeed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=checkFeed(userid="1234userid",activity_id="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.checkingfeed()
# print(y)
@app.route('/checklike')
def check_feed(event=None, context=None):
    try:
        x=checkFeed(userid=event['userid'],activity_id=event['activityid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or activityid is not defined"
        }
        return response
    try:
        y=x.checkingfeed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Commentfeed(userid="1234userid",activityid="77dc977e-3618-11eb-8080-80001ae9b3e2",text="this is post comment")
# y=x.commentingfeed()
# print(y)
@app.route('/commentfeed',methods=["POST"])
def comment_the_feed(event=None, context=None):

    try:
        x=Commentfeed(userid=event['body']['userid'],activityid=event['body']['activityid'],text=event['body']['text'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or activity id is not defined"
        }
        return response
    try:
        y=x.commentingfeed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Get_likes_user(activity_id="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.get_all_likes_user()
# print(y)
@app.route('/likesfeed')
def get_likes_feed(event=None, context=None):

    try:
        x=Get_likes_user(activity_id=event['activityid'])
    except:
        response = {
            "statusCode": 404,
            "body": "activity id is not defined"
        }
        return response
    try:
        y=x.get_all_likes_user()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response


# x=Get_comments_user(activity_id="77dc977e-3618-11eb-8080-80001ae9b3e2")
# y=x.get_all_comments_user()
# print(y)
@app.route('/commentsfeed')
def get_comments_feed(event=None, context=None):

    try:
        x=Get_comments_user(activity_id=event['activityid'])
    except:
        response = {
            "statusCode": 404,
            "body": "activity id is not defined"
        }
        return response
    try:
        y=x.get_all_comments_user()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=UnfollowPage(userid="1234userid",pagename="google")
# y=x.unfollowpages()
# print(y)


@app.route('/unfollowpage',methods=["POST"])
def unfollow_the_page(event=None, context=None):

    try:
        x=UnfollowPage(userid=event['body']['userid'],pagename=event['body']['pagename'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or pagename is not defined"
        }
        return response
    try:
        y=x.unfollowpages()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

@app.route('/followuser',methods=["POST"])
def follow_the_user(event=None, context=None):

    try:
        x=followUser(userid=event['body']['userid'],followuserid=event['body']['followuserid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or follow user id is not defined"
        }
        return response
    try:
        y=x.followusers()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# from unfollow_user import UnfollowUser
# from follow_user import followUser
@app.route('/unfollowuser',methods=["POST"])
def unfollow_the_user(event=None, context=None):

    try:
        x=UnfollowUser(userid=event['body']['userid'],followuserid=event['body']['followuserid'])
    except:
        response = {
            "statusCode": 404,
            "body": "userid or follow user id is not defined"
        }
        return response
    try:
        y=x.unfollowusers()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response

# x=Get_hashtags_Feed(hashtag="google")
# y=x.gethashtags_feed()
# print(y)
@app.route('/hashtagfeed')
def get_the_hashtag_feed(event=None, context=None):
    try:
        x=Get_hashtags_Feed(hashtag=event['hashtag'])
    except:
        response = {
            "statusCode": 404,
            "body": "hashtag is not defined"
        }
        return response
    try:
        y=x.gethashtags_feed()
        response = {
            "statusCode": 200,
            "body": y
        }
        return response
    except:
        response = {
            "statusCode": 400,
            "body": "error parsing your request"
        }
        return response