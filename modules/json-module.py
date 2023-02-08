"""
json module - import json
json- javascript object notation
json - json is a syntax for storing and exchanging data

parse json - convert from Json to python - json.loads
"""
#import json
#import os
#import random

#print(dir(json))
#print(dir(os))
#print(dir(random))

import json

#Json
#x = '{"name":"jasim","age":30,"course":"python"}' # add single quotes '' around the dictionary then it become json
x = {"name":"jasim","age":30,"course":"python"}
print(type(x))
#parsing json to python

#y = json.loads(x)
y = json.dumps(x)
print(type(y))
