"""
implements responses using hack club api
(not sustainable technically)
"""

"""
note: for some reason, you have to use an asyncio-supported requests library.
so no openrouter, you have to use httpx or something
"""
# from openrouter import OpenRouter
import httpx
from primary.util import init_data

def establish_connection():
  """
  returns a function that gets responses from an LLM
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
  
  async def get_responses(prompt):
    """
    gets responses from hack club api
    
    :param prompt: single message prompt
    """
    
    json = {
      "model": model,
      "input": prompt,
      "max_output_tokens": 9000,
      "effort": "minimal"
    }
    
    # make async request
    response = None
    async with httpx.AsyncClient(timeout=None) as client:
      response = await client.post(
        "https://ai.hackclub.com/proxy/v1/responses",
        headers=headers,
        json=json
      )
    
    if response == None or response.status_code != 200:
      return None
    
    response = response.json()
    
    if "output" in response:
      messages = response["output"]
      
      # try to find a message with type=message
      for message in messages:
        if "type" in message and message["type"] == "message":
          return message["content"][0]["text"]
    
    return None
  
  return get_responses

get_responses = establish_connection()