"""
converts latin to shavian
"""

import httpx

async def latin_to_shav(latin_text):
  """
  uses dechifro's transliteration api
  i cannot handle their python code
  
  http://www.dechifro.org/cgi-bin/shave35718.sh
    ?lang=American
    &alphabet=Shavian
    &text=[TEXT]
  """
  
  # prepare request
  url = "http://www.dechifro.org/cgi-bin/shave35718.sh"
  
  params = {
    "lang": "American",
    "alphabet": "Shavian",
    "text": latin_text
  }
  
  # send request
  async with httpx.AsyncClient() as client:
    response = await client.get(url, params=params)
  
  if response.status_code != 200:
    return None
  
  text = response.text
  
  # remove first line (html header)
  response_lines = text.splitlines()
  response_lines.pop(0)
  text = "\n".join(response_lines)
  
  return text.strip()