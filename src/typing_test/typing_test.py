from typing_test.text_gen import generate_word_list
from typing_test.copyproof import copyproof, has_copyproof
from typing_test.results import get_results
import discord
import time

def typing_test_main(bot):
  """
  main function for typing-test module
  """
  
  # users that in a typing test
  # theoretical memory leak if a ton of users never finish tests
  typing_test_users = {}
  
  typing_test_group = bot.create_group("typingtest", "Typing Test-related commands")
  
  @typing_test_group.command(description="Create a new Typing Test")
  async def typing_test(
    ctx,
    script: discord.Option(str, choices=["Latin", "Shavian"])
  ):
    """
    starts a new typing test for the user
    """
    
    # input validation
    if (script not in ["Latin", "Shavian"]):
      await ctx.respond("Invalid script choice")
      return
    
    # if the user is already in a test just overwrite it
    # there is no code to handle it because of how dictionaries work
    
    # string of words
    word_list = generate_word_list(script)
    
    typing_test_users[ctx.author.id] = {
      "script": script,
      "word_list": word_list,
      "timestamp": time.time(),
      "channel_id": ctx.channel.id
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
        f"{author.mention} u cheated! :<"
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
      f"*{author.mention}'s Results*:\n" +
      f"- **{results['wpm']:.2f}** WPM\n" +
      f"- Accuracy: **{results['accuracy']:.2f}%**\n"
    )
  
  @typing_test_group.command(description="Cancel your active Typing Test")
  async def cancel_typing_test(ctx):
    """
    cancels the user's active typing test
    """
    
    if ctx.author.id in typing_test_users:
      del typing_test_users[ctx.author.id]
      await ctx.respond("Your active Typing Test has been cancelled.")
    else:
      await ctx.respond("You do not have an active Typing Test.")