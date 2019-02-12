import json
#todo validate paths to files exist
file = "/etc/passwd"
file2 = "/etc/group"
f1 = open(file, 'r')
f2 = open(file2, 'r')

users = {}
out = {}

def get_group(x):
  groups = []
  for line in f2:
    line = line.strip()
    fields = line.split(":")
    val = int(fields[2])
    if (x == val):
      groups = [fields[0]]
      return groups
    else:
      print(fields[0],fields[2])

def buildJSON(get_group):
  for line in f1:
    line = line.strip()
    fields = line.split(":")
    groups = get_group(int(fields[3]))
    users[fields[0]] = {"full_name": fields[0],"uid": fields[2],"group_name": groups}

buildJSON(get_group)
#todo out this to a json file on local via docker filesys mount
out = json.dumps(users)
      