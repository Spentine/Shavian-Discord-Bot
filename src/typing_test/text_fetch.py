import random

def fetch_word_list(location):
  """
  fetches a list of words from a given text file location
  """
  with open(location, "r", encoding="utf-8") as f:
    words = f.read().splitlines()
  return words

list_locations = {
  "Latin": {
    "200": "src/typing_test/corpus/en-latin/200.txt",
    "1000": "src/typing_test/corpus/en-latin/1000.txt",
  },
  "Shavian": {
    "200": "src/typing_test/corpus/en-shavian/200.txt",
    "1000": "src/typing_test/corpus/en-shavian/1000.txt",
  }
}

def generate_word_list(script="Latin", word_freq="200", count=25):
  """
  generates a word list based off of the arguments provided to user
  
  only "script" because slash command only exposes this
  """
  
  # fetch correct word list
  word_list = fetch_word_list(
    list_locations[script][word_freq]
  )
  
  # generate random list of words
  typing_list = []
  
  for i in range(count):
    typing_list.append(random.choice(word_list))
  
  output = ""
  for word in typing_list:
    output += word + " "
  
  return output.strip()