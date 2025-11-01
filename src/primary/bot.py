from primary.util import retrieve_init_data
from readlex.readlex import readlex_main
from typing_test.typing_test import typing_test_main
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

def main():
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
  
  @bot.command(description="Retrieve latency of bot")
  async def ping(ctx):
    await ctx.respond(f"Latency: {round(bot.latency * 1000)}ms")
  
  @bot.command(description="Help command")
  async def help(ctx):
    await ctx.respond("idk man just use the slash commands lol")