"""
handles console interaction with bot
"""

from primary.bot import primary_main
from dev.text_gen.text_gen import text_gen_main

def request_purpose(options):
  """
  asks user for what they want to do in a menu format
  
  options: list of tuples (option_name: str, option_function: function or None)
  returns: selected option_function or None
  """
  
  # build menu string
  menu = "Shavian-Discord-Bot (ShavBot)\n"
  for i, option in enumerate(options, start=1):
    menu += f"{i}. {option[0]}\n"
  
  # menu
  print(menu, end="")
  
  # until valid input
  while True:
    invalid_choice = "Invalid choice, try again."
    choice = input("Enter choice (1-3): ")
    try:
      choice_int = int(choice)
      if (1 <= choice_int <= len(options)):
        return options[choice_int - 1][1]
      else:
        print(invalid_choice)
    except ValueError:
      print(invalid_choice)

def interaction_main(purpose=None):
  options = [
    ("Start up Discord bot", primary_main),
    ("Run dev/text_gen", text_gen_main),
    ("Exit", None)
  ]
  
  if purpose is not None:
    purpose_func = options[purpose][1]
    purpose_func()
    return
  
  purpose_func = request_purpose(options)
  
  if purpose_func is not None:
    purpose_func()