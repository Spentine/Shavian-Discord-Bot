from readlex.readlex import get_readlex_data
import json
import random

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
  for item in shavian_word_list:
    if (len(item) == 1):
      s += item[0] + "\n"
    else:
      s += " / ".join(item) + "\n"
  
  return s

def fetch_word_list(location):
  """
  fetches a list of words from a given text file location
  """
  with open(location, "r") as f:
    words = f.read().splitlines()
  return words

def generate_word_list(script):
  """
  generates a word list based off of the arguments provided to user
  
  only "script" because slash command only exposes this
  """
  
  # fetch correct word list
  word_list = None
  if script == "Latin":
    word_list = fetch_word_list("src/typing_test/corpus/en-latin/200.txt")
  elif script == "Shavian":
    word_list = fetch_word_list("src/typing_test/corpus/en-shavian/200.txt")
  
  # generate random list of words
  typing_list = []
  count = 25
  
  for i in range(count):
    typing_list.append(random.choice(word_list))
  
  output = ""
  for word in typing_list:
    output += word + " "
  
  return output.strip()