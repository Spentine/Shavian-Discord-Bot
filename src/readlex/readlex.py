def get_readlex_data():
  readlex_location = "src/readlex/readlex.json"
  
  with open(readlex_location, "r") as f:
    readlex_data = json.load(f)
  
  return readlex_data

def readlex_main(bot):
  """
  main function for readlex module
  """
  
  readlex_group = bot.create_group("readlex", "Readlex-related commands")
  
  @readlex_group.command(description="Readlex Test Command")
  async def readlex_test(ctx):
    await ctx.respond("Success")