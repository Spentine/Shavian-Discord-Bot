"""
implements completions using hack club api
"""

import httpx
from primary.util import init_data

def establish_connection():
  """
  returns a function that gets completions from an LLM
  in this case, hack club api
  
  :return: function or None
  """
  
  # check if api key exists
  if "hack_club_api_key" not in init_data:
    return None
  
  # headers for hack club api
  headers = {
    "Authorization": "Bearer " + init_data["hack_club_api_key"],
    "Content-Type": "application/json"
  }
  
  model = "google/gemini-3-pro-preview"
  
  async def get_completions(messages):
    """
    gets completions from hack club api
    
    :param messages: list of message objects
    """
    
    json = {
      "model": model,
      "messages": messages,
      "reasoning": {
        "effort": "minimal",
      }
    }
    
    # make async request
    response = None
    async with httpx.AsyncClient(timeout=None) as client:
      response = await client.post(
        "https://ai.hackclub.com/proxy/v1/chat/completions",
        headers=headers,
        json=json
      )
    
    # print(response.text)
    
    if response == None or response.status_code != 200:
      return None
    
    response = response.json()
    
    return response["choices"][0]["message"]["content"]
  
  return get_completions

get_completions = establish_connection()