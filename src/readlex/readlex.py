from locales.locales import locales, pass_locales
import discord

import json

def get_readlex_converter_data():
  readlex_location = "src/readlex/readlex_converter.json"
  
  with open(readlex_location, "r", encoding="utf-8") as f:
    readlex_data = json.load(f)
  
  return readlex_data


def get_readlex_data():
  readlex_location = "src/readlex/readlex.json"
  
  with open(readlex_location, "r", encoding="utf-8") as f:
    readlex_data = json.load(f)
  
  return readlex_data

readlex_converter_data = get_readlex_converter_data()
readlex_data = get_readlex_data()

def cache_readlex_words():
  latin_cache = {}
  shaw_cache = {}
  for key, arr in readlex_data.items():
    for index, entry in enumerate(arr):
      latin = entry["Latn"]
      shaw = entry["Shaw"]
      
      # check if cache exists
      if latin not in latin_cache:
        latin_cache[latin] = []
      if shaw not in shaw_cache:
        shaw_cache[shaw] = []
      
      # add to cache
      latin_cache[latin].append((key, index))
      shaw_cache[shaw].append((key, index))
      
  return {"latin": latin_cache, "shaw": shaw_cache}

readlex_cache = cache_readlex_words()

def search_readlex(word):
  """
  searches for a word in the ReadLex database
  """
  
  res_script = None # the script to get the results from ("Latn" or "Shaw")
  loc = None # location of results in readlex_data
  
  # search in latin cache
  if word in readlex_cache["latin"]:
    res_script = "Shaw"
    loc = readlex_cache["latin"][word]
  elif word in readlex_cache["shaw"]:
    res_script = "Latn"
    loc = readlex_cache["shaw"][word]
  
  entries = []
  if res_script is not None: # filling entries
    # loc may contain multiple entries
    for entry_loc in loc:
      entry = readlex_data[entry_loc[0]][entry_loc[1]]
      
      # special ipa handling
      ipa = entry["ipa"]
      ipa = ipa.replace("R", "(r)") # optional r-coloring
      
      entries.append({
        "word": entry[res_script],
        "ipa": ipa,
        "pos": entry["pos"]
      })
  
  return entries

def readlex_main(bot):
  """
  main function for readlex module
  """
  
  async def search(ctx, code, word: str, ephemeral: bool = True):
    """
    presents search results from ReadLex for a given word
    """
    
    entries = search_readlex(word)
    
    # create embed
    embed = discord.Embed(
      title=( # pluralize based on number of entries
        (
          locales[code]["readlex"]["search_responses"]["singular_result"]
            .format(word=word)
        ) if len(entries) == 1 else (
          locales[code]["readlex"]["search_responses"]["plural_result"]
            .format(entries=len(entries), word=word)
        )
      ),
      color=discord.Color.blue()
    )
    
    icon_url = "https://readlex.pythonanywhere.com/static/favicon.png"
    embed.set_author(
      name=locales[code]["readlex"]["search_responses"]["author"],
      icon_url=icon_url
    )
    embed.set_footer(text=locales[code]["readlex"]["search_responses"]["footer"])
    
    def add_entry(word, ipa, pos):
      embed.add_field(name=word, value=f"> /{ipa}/\n> *{pos}*", inline=True)
    
    if (len(entries) == 0):
      embed.add_field(
        name=locales[code]["readlex"]["search_responses"]["no_results_found"],
        value=locales[code]["readlex"]["search_responses"]["no_results_found_desc"]
      )
    else:
      for entry in entries:
        # try to use pos_map
        pos = entry["pos"]
        if pos in locales[code]["readlex"]["pos_map"]:
          pos = locales[code]["readlex"]["pos_map"][pos]
        
        add_entry(
          entry["word"],
          entry["ipa"],
          pos
        )
    
    await ctx.respond(embed=embed, ephemeral=ephemeral)
  
  for code in locales:
    locale = locales[code]
    
    # locale function
    word_option = discord.Option(
      str,
      name=locale["readlex"]["search_options"]["word"]["name"],
      description=locale["readlex"]["search_options"]["word"]["description"]
    )
    ephemeral_option = discord.Option(
      str,
      name=locale["readlex"]["search_options"]["ephemeral"]["name"],
      description=locale["readlex"]["search_options"]["ephemeral"]["description"],
      choices=[
        discord.OptionChoice(
          name=locale["readlex"]["search_options"]["ephemeral"]["true"],
          value="true"
        ),
        discord.OptionChoice(
          name=locale["readlex"]["search_options"]["ephemeral"]["false"],
          value="false"
        )
      ]
    )
    
    async def locale_search(
      ctx, code, word: str = word_option, ephemeral: str = ephemeral_option
    ):
      await search(ctx, code, word, ephemeral == "true")
    
    readlex_group = bot.create_group(
      locale["readlex"]["group_command_name"],
      locale["readlex"]["group_command_description"]
    )
    
    readlex_group.command(
      name=locale["readlex"]["search_command_name"],
      description=locale["readlex"]["search_command_description"]
    )(pass_locales(locale_search, code))