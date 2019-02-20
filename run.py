import json
import sys

try:
  file = str(sys.argv[1])
except IndexError:
  file = "/etc/passwd"

try:
  file2 = str(sys.argv[2])
except IndexError:
  file2 = "/etc/group"

outFile = "/mnt/out.json"

try:
  f1 = open(file, 'r')
  f2 = open(file2, 'r')
except IOError:
  print('One or both files not found. If you have arguments, make sure they are formated like this: python run.py /testfile/etc/passwd /testlocation/etc/group')

users = {}

#Finding all of a users groups
def get_group(x):
  groups = []
  for line in f2:
    line = line.strip()
    fields = line.split(":")
    names = fields[3]
    val = names.split(",")
    for v in val:
      if (x == v):
        groups.append(fields[0])
  f2.seek(0)
  return groups

#Entry function and json builder
def buildJSON(get_group):
  for line in f1:
    line = line.strip()
    fields = line.split(":")
    groups = get_group(str(fields[0]))
    users[fields[0]] = {"full_name": fields[0],"uid": fields[2],"group_name": groups}

buildJSON(get_group)

with open(outFile, 'w') as out:
    json.dump(users, out)