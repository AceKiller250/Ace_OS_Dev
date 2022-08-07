import os
import sys 
import json



pathname = os.path.dirname(sys.argv[0])
foldername = os.path.abspath(pathname)

f = open(foldername + "/version.json")

data = json.load(f)

print(data.get("version"))

f.close()