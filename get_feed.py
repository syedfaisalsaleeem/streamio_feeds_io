import json
import stream

user_id="1234userid"
client = stream.connect('q2hzgpctc2e5', 'cgrx2vxsy6kmr4m76mt648azhfcucjkyev2v27au2envsgujxer3zs62fpwtm4xb')
feed = client.feed('timeline', user_id)
activities = feed.get()
print(activities)