import json
from pandas.io.json import json_normalize

with open('path_to_json.json') as f:
  data = json.load(f)
  df = json_normalize(data, record_path=['features'], meta=['name']) 

print(df)