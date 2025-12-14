"""
detect script of a given text
"""

# shavian characters
shavian_chars = set(
  list("𐑦𐑑𐑩𐑕𐑯𐑤𐑒𐑛𐑟𐑮𐑐𐑥𐑼𐑨𐑧𐑚𐑱𐑙𐑓𐑲𐑪𐑴𐑳𐑰𐑜𐑖𐑝𐑢𐑡𐑣𐑻𐑹𐑵𐑗𐑸𐑬𐑿𐑫𐑭𐑷𐑔𐑾𐑘𐑺𐑽𐑶𐑞𐑠")
)

def detect_script(text):
  # count number of shavian vs non-shavian characters
  shavian_count = 0
  non_shavian_count = 0
  for char in text:
    if char in shavian_chars:
      shavian_count += 1
    else:
      non_shavian_count += 1
  
  # determine script based on counts
  if shavian_count > non_shavian_count:
    return "Shavian"
  else:
    return "Latin"