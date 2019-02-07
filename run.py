import json

file = "/etc/passwd"
file_object = open(file, 'r')

users = {}

out = {}
for line in file_object:
     line = line.strip()
     fields = line.split(":")
     users[fields[0]] = fields[-1]
     out = json.dumps(users)


     

