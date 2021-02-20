import json


x = 15
y = "Just a string"
z = [1,3,6,9]

print(json.dumps([x,y,z]))

testdict = { "a":1, "b":3, "c":2}

s = json.dumps(testdict, indent=4)
print(s)
d = json.loads(s)
d["c"]

