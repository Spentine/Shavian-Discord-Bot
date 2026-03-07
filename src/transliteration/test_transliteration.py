import asyncio
from transliteration.latin_to_shav import latin_to_shav
from transliteration.shav_to_latin import shav_to_latin

def test_transliteration_main():
  asyncio.run(request())

async def request():
  print("Enter script to transliterate to:"
        "\n1. Shavian"
        "\n2. Latin")
  while True:
    choice = input("Enter choice (1-2): ")
    print()
    
    if choice == "1":
      text = input("Enter Latin text to transliterate to Shavian: ")
      print(await latin_to_shav(text))
    elif choice == "2":
      text = input("Enter Shavian text to transliterate to Latin: ")
      print(await shav_to_latin(text))
    else:
      print("Invalid choice, try again.")
    
    print()