from typing_test.myers import diff

def get_results(text, correct, elapsed_time):
  """
  compares user-typed text to the correct text
  returns results as a dictionary
  """
  
  # get diff
  differences = diff(correct, text)
  
  # calculate raw wpm
  raw_wpm = (len(text) / 5) / elapsed_time * 60
  
  # calculate accuracy
  accuracy = min(
    1.0,
    (len(correct) - len(differences)) / len(correct)
  )
  
  results = {
    "differences": differences,
    "accuracy": accuracy * 100,
    
    # wpm = cpm / 5
    "wpm": raw_wpm * accuracy,
    "raw_wpm": raw_wpm
  }
  
  return results