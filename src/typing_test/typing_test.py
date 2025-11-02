from locales.locales import locales, pass_locales
from typing_test.text_gen import generate_word_list
from typing_test.copyproof import copyproof, has_copyproof
from typing_test.results import get_results

from functools import partial
import json
import discord
import time

def typing_test_main(bot):
  """
  main function for typing-test module
  """
  
  # users that in a typing test
  # theoretical memory leak if a ton of users never finish tests
  typing_test_users = {}
  
  async def typing_test(
    ctx,
    code,
    script: discord.Option(str, choices=["Latin", "Shavian"])
  ):
    """
    starts a new typing test for the user
    """
    
    # input validation
    if (script not in ["Latin", "Shavian"]):
      await ctx.respond(
        locales[code]["typing_test"]["start_responses"]["invalid_script"]
      )
      return
    
    # if the user is already in a test just overwrite it
    # there is no code to handle it because of how dictionaries work
    
    # string of words
    word_list = generate_word_list(script)
    
    typing_test_users[ctx.author.id] = {
      "script": script,
      "word_list": word_list,
      "timestamp": time.time(),
      "channel_id": ctx.channel.id,
      "code": code
    }

    await ctx.respond(
      "```\n" + copyproof(word_list) + "\n```"
    )
  
  @bot.register_on_message
  async def on_message(message):
    """
    checks messages for typing test answers
    """
    
    # get author and check
    author = message.author
    if author.id not in typing_test_users:
      return
    
    test_data = typing_test_users[author.id]
    code = test_data["code"]
    
    # check channel
    if message.channel.id != test_data["channel_id"]:
      return
    
    # check time
    current_time = time.time()
    
    # expire after 1 hour
    if current_time - test_data["timestamp"] > (3600):
      del typing_test_users[author.id]
      return
    
    # check copyproof
    if has_copyproof(message.content):
      await message.channel.send(
        locales[code]["typing_test"]["on_message_responses"]["cheated"]
          .format(mention=author.mention)
      )
      del typing_test_users[author.id]
      return
    
    # compare results
    results = get_results(
      message.content,
      test_data["word_list"],
      current_time - test_data["timestamp"]
    )
    
    # delete user from active tests
    del typing_test_users[author.id]
    
    # send results
    await message.channel.send(
      locales[code]["typing_test"]["on_message_responses"]["results"]
        .format(
          mention=author.mention,
          wpm=results["wpm"],
          accuracy=results["accuracy"],
        )
    )
  
  async def cancel_typing_test(ctx, code):
    """
    cancels the user's active typing test
    """
    
    if ctx.author.id in typing_test_users:
      del typing_test_users[ctx.author.id]
      await ctx.respond(locales[code]["typing_test"]["cancel_responses"]["cancelled"])
    else:
      await ctx.respond(locales[code]["typing_test"]["cancel_responses"]["not_active"])

  for code in locales:
    locale = locales[code]
  
    typing_group = bot.create_group(
      locale["typing_test"]["group_command_name"],
      locale["typing_test"]["group_command_description"]
    )
    
    typing_group.command(
      name=locale["typing_test"]["start_command_name"],
      description=locale["typing_test"]["start_command_description"]
    )(pass_locales(typing_test, code))
    typing_group.command(
      name=locale["typing_test"]["cancel_command_name"],
      description=locale["typing_test"]["cancel_command_description"]
    )(pass_locales(cancel_typing_test, code))