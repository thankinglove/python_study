__author__ = "Alex Li"
import json

f = open("test.text", "r")

# data = json.loads(f.read()) #data = pickle.loads(f.read())
data = json.load(f)
print(data)
f.close()

# for line in f:
#     print(json.loads(line))
