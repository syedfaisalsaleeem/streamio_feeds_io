import requests
import pprint
x=requests.post(url="https://9q2d566izk.execute-api.us-east-1.amazonaws.com/dev/createpost",
	data={

    "user_id":"1234userid",
    "summary":"here is faisal #faisal",
    "url":"urlno",
    "image":"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"
	

	})

print(x)
pprint.pprint(vars(x))

# ####### Values for S3 object Bucket Policy #####
# [
#                 "s3:PutObject",
#                 "s3:GetObject",
#                 "s3:DeleteObject",
#                 "s3:PutObjectAcl",
#                 "s3:GetObjectAcl",
#             ],