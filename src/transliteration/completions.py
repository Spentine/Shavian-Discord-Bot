"""
implements completions using hack club api
(not sustainable technically)
"""

from openrouter import OpenRouter
from primary.util import init_data

def establish_connection():
  # create client
  client = OpenRouter(
    api_key = init_data["hack_club_api_key"],
    server_url = "https://ai.hackclub.com/proxy/v1"
  )
  
  model = "google/gemini-3-pro-preview"
  def get_completions(messages):
    """
    get completion from hack club
    """
    response = client.chat.send(
      model = model,
      messages = messages,
      stream = False,
      temperature = 0.1
    )
    
    return response.choices[0].message.content
  
  return get_completions

get_completions = establish_connection()