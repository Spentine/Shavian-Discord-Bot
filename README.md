# Shavian Discord Bot (ShavBot)

*Created by Spentine Nov 1*

## Usage and Installation

1. Install or use a Python version compatible with the project requirements. 
    - (supporting Python 3.11 because it is the installation on my Linux machine)
2. Clone the GitHub repository to your local device.
3. Move your current working directory to the repository folder.
4. Install the requirements with `pip install -r requirements.txt`
5. Edit `data.json` to update the information for your bot.
6. Execute `src/main.py`.

Once you execute the Python file, you will be greeted with a request to enter your bot's Discord token, which will be stored in `secrets.json`. On all future executions, this will no longer appear (of course).

### Important Note About Responses API

The LLM API in use to power the transliteration engine from Shavian to Latin is provided by the **Hack Club** foundation. However, to use their API, the developer *must be in high school*. The only reason it was chosen was because it is completely free (*as of 14 December 2025*), making it, of course, the best choice for AI hosting.

However, not everybody is a teenager. In this case, the `src/transliteration/responses.py` file can be modified to provide an alternate `establish_connection -> get_responses` function. As mentioned in the file, *it must be asynchronous*, otherwise, the entire program may be suspended by the ongoing transliteration function.

## `secrets.json`

```py
{
  "token": # Discord Bot Token
  "hack_club_api_key": # For more information, go to [ai.hackclub.com]
}
```

## `data.json`

```py
{
  # The User IDs of the accounts permitted to use the transliteration feature.
  "transliteration": # <Discord User ID>[]
  
  # The Emojis in use by the bot.
  "emojis": {
    "loading": # The markdown text of the emoji.
  }
}
```

## Personal Narrative

I have wanted to create this bot for months, but I decided not to so that I wasn't forcing my ideas on others. One day, a friend from the server expressed their desire for a Shavian equaivalent of a fun typing test in a Discord bot. I shared my interest in it too, and realized — this is probably the time I should finally make a bot, not just with the typing test, but with other features the server may find useful.
