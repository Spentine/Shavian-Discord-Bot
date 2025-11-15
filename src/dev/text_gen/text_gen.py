"""
this is a tool to make creating shavian word lists easier
"""

from readlex.readlex import get_readlex_data
from typing_test.text_fetch import fetch_word_list
import json

def convert_to_shavian_list(word_list):
  """
  converts a list of words to their shavian script equivalent
  if there are any words with two pronunciations (homographs), it displays both options
  
  meant more as a pre-production utility than anything else
  """
  
  readlex_data = get_readlex_data()
  
  shavian_word_list = []
  
  # get shavian equivalents
  for word in word_list:
    if word in readlex_data:
      data = readlex_data[word]
      options = []
      for entry in data:
        options.append(entry["Shaw"])
      shavian_word_list.append(options)
    else:
      shavian_word_list.append([word])
  
  # format output
  s = ""
  for index, item in enumerate(shavian_word_list):
    if (len(item) == 1):
      s += item[0] + "\n"
    else:
      s += f"{' / '.join(item)} ('+ word_list[index] + ')\n"
  
  return s

def from_monkeytype(json_str):
  # load the actual json object
  obj = json.loads(json_str)
  
  # get ["words"] list
  words = obj["words"]
  return words

def text_gen_main():
  with open("src/dev/text_gen/monkeytype.json", "r", encoding="utf-8") as f:
    json_str = f.read()
  word_list = from_monkeytype(json_str)
  shavian_word_list = convert_to_shavian_list(word_list)
  
  with open("src/dev/text_gen/en.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(word_list))
  
  with open("src/dev/text_gen/en-shavian.txt", "w", encoding="utf-8") as f:
    f.write(shavian_word_list)
  