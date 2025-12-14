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
    
    transliterate_info = locales[code]["transliteration"]["transliterate_responses"]
    
    # check access
    if ctx.author.id not in generic_data.get("transliteration_access", []):
      await ctx.respond(transliterate_info["no_access"], ephemeral=True)
      return
    
    # reply with loading message
    message = await ctx.respond(
      transliterate_info["loading"]
        .format(loading_emoji=generic_data["emojis"]["loading"]),
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
        await message.edit(content=transliterate_info["error"])
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
  
  for code in locales:
    locale = locales[code]
    
    to_info = locale["transliteration"]["transliterate_options"]["to"]
    text_info = locale["transliteration"]["transliterate_options"]["text"]
    
    to_option = discord.Option(
      str,
      name=to_info["name"],
      description=to_info["description"],
      choices=[
        discord.OptionChoice(
          name=to_info["latin"],
          value="Latin"
        ),
        discord.OptionChoice(
          name=to_info["shavian"],
          value="Shavian"
        )
      ]
    )
    text_option = discord.Option(
      str,
      name=text_info["name"],
      description=text_info["description"]
    )
    
    async def locale_transliterate(
      ctx, code, to: str = to_option, text: str = text_option
    ):
      await transliterate(ctx, code, to, text)
    
    async def locale_transliterate_last(ctx, code):
      await transliterate_last(ctx, code)
    
    transliteration_group = bot.create_group(
      locale["transliteration"]["group_command_name"],
      locale["transliteration"]["group_command_description"]
    )
    
    transliteration_group.command(
      name=locale["transliteration"]["transliterate_command_name"],
      description=locale["transliteration"]["transliterate_command_description"]
    )(pass_locales(locale_transliterate, code))
    
    transliteration_group.command(
      name=locale["transliteration"]["transliterate_last_command_name"],
      description=locale["transliteration"]["transliterate_last_command_description"]
    )(pass_locales(locale_transliterate_last, code))