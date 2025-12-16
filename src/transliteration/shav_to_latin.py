# responses deprecated, consider removal
from transliteration.responses import get_responses
from transliteration.completions import get_completions

async def shav_to_latin(shavian_text, type="completions"):
  """
  transliterates shavian to latin using responses/completions api
  i'm not smart enough to engineer a more robust solution without it
  """
  
  if type == "completions":
    # check if completions available
    if not get_completions:
      return None
    
    # use completions api
    messages = [
      {
        "role": "system",
        "content": (
          "You are a transliteration engine that converts text from Shavian script to Latin script. "
          "You must only respond with the transliterated text, and nothing else. Do not think either, just answer directly. "
          "Miscellaneous characters: · (Namer Dot) is for proper nouns, and ⸰ (Acronym Dot) is for acronyms."
        )
      },
      {
        "role": "user",
        "content": (
          "Transliterate the following text to Standard English Orthography:\n\n" + shavian_text
        )
      }
    ]
    
    return await get_completions(messages)
  elif type == "responses":
    # check if responses available
    if not get_responses:
      return None
    
    # use responses api
    prompt = "You are a transliteration engine that converts text from Shavian script to Latin script. You must only respond with the transliterated text, and nothing else. Do not think either, just answer directly.\n\n" + "Transliterate the following text to Standard English Orthography:\n\n" + shavian_text
    
    return await get_responses(prompt)
  
  return None