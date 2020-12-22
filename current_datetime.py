# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# # print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

import re

# similar to hashtag.py this regex finds username mentions, with a very permissive 
# algorithm, suitable for MediaWiki/Wikipedia usernames, which can include 
# unicode symbols and punctuation (almost anything but whitespace and a 
# few punctuation marks)

# mention_re = re.compile("(?:^|\s)[＠ @]{1}([^\s#<>[\]|{}]+)", re.UNICODE)
# summary="asdda #123455 #123455"
# y=re.findall(r"(?:^|\s)[＠ @]{1}([^\s#<>[\]|{}]+)",summary)
# print(y)
# y=re.findall(r"#(\w+)", summary)
# print(y)
import re
summary="asdda #123455 #123455 #231234"
x=list([re.sub(r"(\W+)$", "", j) for j in set([i for i in summary.split() if i.startswith("#")])])
# set(['#people', '#helpful', '#stackoverflow'])
print(x)
temp_list=[]
for values in x:
	val="hashtag:"+values[1:]
	temp_list.append(val)
print(temp_list)
# import re 
  
# # function to print all the hashtags in a text 
# def extract_hashtags(text): 
      
#     # the regular expression 
#     regex = "#(\w+)"
      
#     # extracting the hashtags 
#     hashtag_list = re.findall(regex, text) 
      
#     # printing the hashtag_list 
#     print("The hashtags in \"" + text + "\" are :") 
#     for hashtag in hashtag_list: 
#         print(hashtag) 
  
# if __name__=="__main__": 
#     text1 = "GeeksforGeeks is a wonderful # website for # ComputerScience"
#     text2 = "This day is beautiful ! # instagood # photooftheday # cute"
#     extract_hashtags(text1) 
#     extract_hashtags(text2) 