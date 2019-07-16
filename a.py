import json
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
print(s)
print(type(s))
json_acceptable_string = s.replace("'", "\"")
print(type(json_acceptable_string))
print(json_acceptable_string)
d = json.loads(json_acceptable_string)
print(type(d))
