import json

def construct_file(data_location):
  """
  constructs a secrets file from user input
  
  returns the constructed data as a dictionary
  """
  
  # get token (the only required data for now)
  print("Enter token: ", end="")
  token = input().strip()
  data = { "token": token }
  
  # write data to file
  try:
    f = open(data_location, "w")
    f.write(json.dumps(data, indent=2))
    f.close()
    print(f"Data file created at: {data_location}")
  except Exception as e:
    print(f"Error writing data file: {e}")
  
  return data

def retrieve_init_data(data_location):
  """
  retrieves necessary data from a secrets file located in `data_location`
  """
  
  data = None
  data_file = None
  
  # try to retrieve the file
  try:
    f = open(data_location, "r")
    data_file = f.read().strip()
    f.close()
  except FileNotFoundError:
    print(f"Data file not found: {data_location}")
  except Exception as e:
    print(f"Error reading data file: {e}")
  
  if data_file:
    try:
      data = json.loads(data_file)
    except json.JSONDecodeError as e:
      print(f"Error parsing JSON data: {e}")
  else:
    print("No data file found, constructing a new one.")
    data = construct_file(data_location)
  
  return data