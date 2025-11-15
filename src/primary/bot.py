from locales.locales import locales, pass_locales
from primary.util import retrieve_init_data
from readlex.readlex import readlex_main
from typing_test.typing_test import typing_test_main

from functools import partial
import discord

class ShavBot(discord.Bot):
  """
  main bot class
  """
  
  # for extra features
  def __init__(self, **options):
    super().__init__(**options)
    
    self.on_message_callbacks = []
  
  async def on_ready(self):
    print(f"Logged in as {self.user} (ID: {self.user.id})")
  
  async def on_message(self, message):
    # default on_message behavior
    print(f"Message from {message.author}: {message.content}")
    
    # call extra on_message callbacks
    for callback in self.on_message_callbacks:
      await callback(message)
  
  def register_on_message(self, func):
    self.on_message_callbacks.append(func)

def primary_main():
  init_data = retrieve_init_data("secrets.json")
  
  intents = discord.Intents.all()
  bot = ShavBot(intents=intents)
  
  primary_interactions(bot)
  # readlex_main(bot) # not implemented yet
  typing_test_main(bot)
  
  bot.run(init_data["token"])

def primary_interactions(bot):
  """
  provides primary bot interactions mainly for testing purposes
  """
  
  async def ping(ctx, code):
    await ctx.respond(
      locales[code]["ping_response"]
        .format(latency=bot.latency*1000)
    )
  
  async def help(ctx, code):
    await ctx.respond(
      locales[code]["help_response"]
    )
  
  # register commands
  for code in locales:
    locale = locales[code]
    
    bot.command(
      name=locale["ping_command_name"],
      description=locale["ping_command_description"]
    )(pass_locales(ping, code))
    bot.command(
      name=locale["help_command_name"],
      description=locale["help_command_description"]
    )(pass_locales(help, code))