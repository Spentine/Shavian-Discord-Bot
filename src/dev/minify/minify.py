"""
this file just minifies a json

it's a really big json though so it's difficult to actually use online tools
"""

import json

def minify_json(input_location, output_location):
  with open(input_location, "r", encoding="utf-8") as f:
    data = json.load(f)
  
  with open(output_location, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

# minify_json("src/dev/minify/readlex.json", "src/readlex/readlex_m.json")