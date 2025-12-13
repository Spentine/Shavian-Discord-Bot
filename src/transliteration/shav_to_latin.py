from transliteration.completions import get_completions

def shav_to_latin(shavian_text):
  """
  transliterates shavian to latin using completions api
  i'm not smart enough to engineer a more robust solution without it
  """
  
  messages = [
    {
      "role": "system",
      "content": (
        "You are a transliteration engine that converts text from Shavian script to Latin script. You must only respond with the transliterated text, and nothing else. Do not use thinking either, just answer directly."
      )
    },
    {
      "role": "user",
      "content": shavian_text
    }
  ]
  
  return get_completions(messages)

def transliteration_main():
  # res = shav_to_latin("𐑕𐑐𐑨𐑥𐑼𐑟 𐑑𐑸𐑜𐑩𐑑 𐑢𐑳𐑑𐑧𐑝𐑼 𐑐𐑰𐑐𐑩𐑤 𐑸 𐑿𐑟𐑦𐑙. 𐑰𐑥𐑱𐑤, 𐑕𐑴𐑖𐑩𐑤 𐑥𐑰𐑛𐑾, 𐑮𐑧𐑜𐑘𐑩𐑤𐑼 𐑥𐑱𐑤, 𐑓𐑴𐑯 𐑒𐑷𐑤𐑟... 𐑷𐑤 𐑿𐑟𐑛 𐑑 𐑚𐑰 𐑿𐑕𐑓𐑩𐑤. 𐑢𐑰 𐑒𐑰𐑐 𐑗𐑱𐑯𐑡𐑦𐑙 𐑢𐑳𐑑 𐑢𐑰 𐑿𐑟 𐑑 𐑦𐑕𐑒𐑱𐑐 𐑞 𐑕𐑐𐑨⁠⁠𐑥 𐑚𐑳𐑑 𐑦𐑑 𐑒𐑰𐑐𐑕 𐑓𐑪𐑤𐑴𐑦𐑙 𐑳𐑕")
  res = shav_to_latin("𐑮𐑲𐑑, 𐑞𐑨𐑑'𐑕 𐑦𐑯 𐑐𐑸𐑑 𐑢𐑲 𐑲 𐑷𐑕𐑒, 𐑚𐑦𐑒𐑪𐑟 𐑲 𐑮𐑾𐑤𐑦 𐑕𐑑𐑮𐑳𐑜𐑩𐑤 𐑢𐑦𐑞 𐑕𐑐𐑱𐑕𐑦𐑙. 𐑲 𐑢𐑦𐑖 𐑞𐑺 𐑢𐑪𐑟 𐑩 𐑒𐑪𐑥𐑪𐑯 𐑮𐑵𐑤𐑦𐑙 𐑞𐑨𐑑 𐑣𐑨𐑛 𐑕𐑐𐑱𐑕 𐑨𐑤𐑴𐑒𐑱𐑑𐑩𐑛 𐑓 𐑩𐑕𐑧𐑯𐑛𐑼𐑟 𐑯 𐑛𐑰𐑕𐑧𐑯𐑛𐑼𐑟 𐑕𐑴 𐑿 𐑛𐑴𐑯𐑑 𐑷𐑤𐑢𐑱𐑟 𐑣𐑨𐑝 𐑞𐑧𐑥 𐑒𐑩𐑤𐑲𐑛𐑦𐑙\n𐑦𐑑 𐑕𐑰𐑥𐑕 𐑷𐑤 𐑝 𐑞 𐑤𐑧𐑑𐑼𐑟 𐑸 𐑛𐑦𐑕𐑑𐑦𐑙𐑒𐑑 𐑕𐑑𐑦𐑤, 𐑚𐑳𐑑 𐑞𐑱 𐑸 𐑤𐑧𐑕 𐑮𐑧𐑒𐑩𐑜𐑯𐑲𐑟𐑦𐑚𐑩𐑤 𐑑 𐑥𐑰 𐑕𐑴 𐑮𐑰𐑛𐑦𐑙 𐑦𐑟 𐑕𐑤𐑴𐑼")
  
  print(res)