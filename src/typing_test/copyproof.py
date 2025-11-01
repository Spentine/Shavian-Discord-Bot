invisible_char = "\u200d" # zero width joiner

def copyproof(text):
  """
  copyproofs a text by inserting invisible characters between each word
  
  makes it possible to detect copied text
  """

  return (
    invisible_char
  ).join(text)

def has_copyproof(text):
  """
  checks if the text is copyproofed by looking for invisible characters
  """
  
  return invisible_char in text