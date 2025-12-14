from transliteration.responses import get_responses

async def shav_to_latin(shavian_text):
  """
  transliterates shavian to latin using completions api
  i'm not smart enough to engineer a more robust solution without it
  """
  
  # check if responses available
  if not get_responses:
    return None
  
  # use responses api
  prompt = "You are a transliteration engine that converts text from Shavian script to Latin script. You must only respond with the transliterated text, and nothing else. Do not think either, just answer directly.\n\n" + "Transliterate the following text to Standard English Orthography:\n\n" + shavian_text
  
  return await get_responses(prompt)