import json
import inspect
from functools import partial, update_wrapper

locale_locations = {
  "en": "src/locales/en.json",
  "shaw": "src/locales/shaw.json"
}

def load_locale(locale_code):
  """
  loads locale data from code by getting file
  """
  
  if locale_code not in locale_locations:
    raise ValueError(f"Locale '{locale_code}' not found.")
  
  with open(locale_locations[locale_code], "r", encoding="utf-8") as f:
    locale_data = json.load(f)
  
  return locale_data

def load_locales():
  """
  loads all locales into the locales dict
  """
  
  locales = {}
  for code in locale_locations:
    locales[code] = load_locale(code)

  return locales

# AI-GENERATED FUNCTION
# there is absolutely no way i will be able to write this myself
# circumvents python's late binding in closures
def pass_locales(func, code):
  """
  decorator to pass locale data to command functions
  """
  
  # Create the partial function
  wrapper = partial(func, code=code)
  
  # Copy function attributes
  update_wrapper(wrapper, func)
  
  # Remove 'code' from the signature
  sig = inspect.signature(func)
  new_params = [p for p in sig.parameters.values() if p.name != 'code']
  wrapper.__signature__ = sig.replace(parameters=new_params)
  
  return wrapper

locales = load_locales()