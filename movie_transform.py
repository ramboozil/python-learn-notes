import sys
import datetime
import json

line='{"movie":"2797","rate":"4","timeStamp":"978302039","uid":"1"}'
line = line.strip()
hjson = json.loads(line)
movie = hjson['movie']
rate = hjson['rate']
timeStamp = hjson['timeStamp']
uid = hjson['uid']
timeStamp = datetime.datetime.fromtimestamp(float(timeStamp))
print('\t'.join([movie, rate, str(timeStamp), uid]))

print('hello','world')