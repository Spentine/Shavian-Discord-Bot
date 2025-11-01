def get_results(text, correct, elapsed_time):
  """
  compares user-typed text to the correct text
  returns results as a dictionary
  """
  
  # split into words
  text_words = text.split()
  correct_words = correct.split()
  
  total_words = len(correct_words)
  actual_words = min(len(text_words), len(correct_words))
  correct_count = 0
  incorrect_words = []
  
  # count correct words
  for i in range(actual_words):
    if text_words[i] == correct_words[i]:
      correct_count += 1
    else:
      incorrect_words.append((text_words[i], correct_words[i]))
  
  # calculate accuracy
  accuracy = 0
  if total_words > 0:
    accuracy = (correct_count / total_words)
  
  # calculate raw wpm
  raw_wpm = (len(text) / 5) / elapsed_time * 60
  
  results = {
    "total_words": total_words,
    "correct_count": correct_count,
    "accuracy": accuracy * 100,
    "incorrect_words": incorrect_words,
    
    # wpm = cpm / 5
    "wpm": raw_wpm * accuracy,
    "raw_wpm": raw_wpm
  }
  
  return results