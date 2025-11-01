from primary.util import retrieve_init_data
import discord

class ShavBot(discord.Client):
  async def on_ready(self):
    print(f"Logged in as {self.user} (ID: {self.user.id})")
  
  async def on_message(self, message):
    print(f"Message from {message.author}: {message.content}")

def main():
  init_data = retrieve_init_data("secrets.json")
  
  intents = discord.Intents.all()
  client = ShavBot(intents=intents)
  client.run(init_data["token"])