import json
from flask import Flask,request,jsonify
from post_like import Postlike
from creating_feed import Creating_Feed
from socialsection.trendinghashtags import trendinghashtags
app = Flask(__name__)

# event="tempevent"
# context="tempcontext"
# @raven.capture_exceptions

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
    # if request.method == 'POST':
    try:
        user_id="ac211c30-ffdd-40af-9402-d3b36a671a7b"
        activity_id="5f09e455-1fa0-11eb-bec3-128a130028af"
        print(event)
        x=Postlike(event['userid'],event['activityid'])
        # x=Postlike("ac211c30-ffdd-40af-9402-d3b36a671a7b","5f09e455-1fa0-11eb-bec3-128a130028af")
        y=x.get_no_like()
        print(y)
        # return do_the_login()
        # else:
        #     return show_the_login_form()
        # arg1=request.args['arg1']
        body = {
            "message": "Go Serverless v1.0! Your function executed successfully!",
            "input": y,
            "input2":event
            # "input2":event.foo
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
        # return "error in body"
    try:
        x.capturehashtag()
    except:
        response = {
            "statusCode": 400,
            "body": "error in summary"
        }
        return response
        # return "error in summary"
    try:
        x.storingimages3()
    except:
        response = {
            "statusCode": 400,
            "body": "can't store image"
        }
        return response
        # return "can't store image"
    # x.dynamodbquery()
    try:
        x.dynamodbquery()
    except:
        response = {
            "statusCode": 400,
            "body": "can't query dynamo db"
        }
        return response
        # return "can't query dynamo db"
    # x.create()
    # y=x.create()
    # response = {
    #         "statusCode": 200,
    #         "body": y
    #     }
    # return response
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
        # return "feed is not created"


    #parameters for request for create post
    # userid=""
    # summary=""
    # image=""
    # url=""
    
    
    # if request.method == 'POST':
    # user_id = request.json.get('userId')
    # name = request.json.get('name')
    # if not user_id or not name:
    #     return jsonify({'error': 'Please provide userId and name'}), 400
    # try:

    #     body = {
    #         "message": "Go Serverless v1.0! Your function executed successfully!",
    #         "input2":event['body']['user_id']
    #         # "input2":event.foo
    #     }

    #     response = {
    #         "statusCode": 200,
    #         "body": body
    #     }
    #     return response

    #     # return jsonify({
    #     # 'userId': user_id,
    #     # 'name': name,
    #     # "statusCode":200,
    #     # "event":event
    #     # })
    # except:
    #     response = {
    #         "statusCode": 404,
    #         "body": "invalid parameters"
    #     }

    #     return response