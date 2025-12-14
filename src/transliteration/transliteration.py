from locales.locales import locales, pass_locales
from transliteration.latin_to_shav import latin_to_shav
from transliteration.shav_to_latin import shav_to_latin
from transliteration.detect_script import detect_script
import discord

from primary.util import generic_data

def transliteration_main(bot):
  """
  main function for transliteration module
  """
  
  async def transliterate(ctx, code: str, to: str, text: str):
    """
    transliterates text
    """
    
    # check access
    if ctx.author.id not in generic_data.get("transliteration_access", []):
      await ctx.respond("You do not have access to this command.", ephemeral=True)
      return
    
    # reply with loading message
    message = await ctx.respond(
      "Transliterating... " + generic_data["emojis"]["loading"],
      ephemeral=True
    )
    
    async def do_transliteration():
      # transliterate
      if to == "Shavian":
        result = await latin_to_shav(text)
      else:
        result = await shav_to_latin(text)
      
      # check for errors
      if not result:
        await message.edit(content="An error occurred during transliteration.")
        return
      
      await message.edit(content=result)
    
    # spawn transliteration task
    # do not await directly to prevent blocking
    bot.loop.create_task(do_transliteration())
  
  async def transliterate_last(ctx, code: str):
    """
    transliterates the last message in the channel
    """
    
    # get the channel
    channel = ctx.channel
    
    # fetch last message
    last_message = await channel.fetch_message(channel.last_message_id)
    
    # get text
    text = last_message.content
    
    # detect script
    script = detect_script(text)
    
    to_script = "Shavian" if script == "Latin" else "Latin"
    
    # use transliterate function
    await transliterate(ctx, code, to_script, text)
  
  code = "en"
  
  to_option = discord.Option(
    str,
    name="to",
    description="The script to transliterate to",
    choices=[
      discord.OptionChoice(
        name="Latin",
        value="Latin"
      ),
      discord.OptionChoice(
        name="Shavian",
        value="Shavian"
      )
    ]
  )
  text_option = discord.Option(
    str,
    name="text",
    description="The text to transliterate"
  )
  
  async def locale_transliterate(
    ctx, code, to: str = to_option, text: str = text_option
  ):
    await transliterate(ctx, code, to, text)
  
  async def locale_transliterate_last(ctx, code):
    await transliterate_last(ctx, code)
  
  transliteration_group = bot.create_group(
    "transliteration",
    "Commands for transliterating text between Latin and Shavian scripts"
  )
  
  transliteration_group.command(
    name="transliterate",
    description="Transliterate text between Latin and Shavian scripts"
  )(pass_locales(locale_transliterate, code))
  
  transliteration_group.command(
    name="transliterate_last",
    description="Transliterate the last message in the channel between Latin and Shavian scripts"
  )(pass_locales(locale_transliterate_last, code))