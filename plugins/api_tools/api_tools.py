#!/usr/bin/python
import requests
import json

# https://cors-shane0.vercel.app/api/day

def extract_number_from_json_or_dict(input_data):
    """
    Extracts the number from a JSON object or dictionary with a single key-value pair.

    Parameters:
        input_data (str | dict): A JSON string or a dictionary.

    Returns:
        int: The extracted number.

    Raises:
        ValueError: If the input is not a valid JSON string or dictionary with a single key-value pair.
    """
    if isinstance(input_data, str):  # Check if it's a JSON string
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON string.") from e
    elif isinstance(input_data, dict):  # Already a dictionary
        data = input_data
    else:
        raise ValueError("Input must be a JSON string or a dictionary.")

    if isinstance(data, dict) and len(data) == 1:
        return next(iter(data.values()))
    raise ValueError("Input must contain exactly one key-value pair.")

def get_api_data(url):
  """
  Fetches data from the provided API URL and returns a dictionary.

  Args:
      url: The URL of the API endpoint.

  Returns:
      A dictionary containing the API response data, or None on error.
  """
  response = requests.get(url)
  if response.status_code == 200:
    try:
      data = response.json()
      return data
    except:
      print(f"Error: Couldn't parse response as JSON.")
      return None
  else:
    print(f"Error: API request failed with status code {response.status_code}")
    return None

# def get_endpoint(base_url):
  # Define the base URL (replace with your actual base URL)
  # base_url = "http://ms.ons.pnet/ahs/api/"

  # Prompt user for endpoint name (replace with placeholder if needed)
  # endpoint_name = input("Enter the API endpoint name (e.g., day): ")

  # Construct the full URL
  # url = f"{base_url}{endpoint_name}"

  # Get data from the API
  # data = get_api_data(url)

  # Check if data retrieval was successful
  # if data is None:
  #   return

  # List available keys with enumeration
  # print("\nAvailable keys:")
  # keys = list(data.keys())
  # for i, key in enumerate(keys):
  #   print(f"{i+1}. {key}")

  # Prompt user for key selection
  # while True:
  #   try:
  #     choice = int(input("\nEnter the number corresponding to the desired key: "))
  #     if 0 < choice <= len(keys):
  #       break
  #     else:
  #       print("Invalid choice. Please enter a number between 1 and", len(keys))
  #   except ValueError:
  #     print("Invalid input. Please enter a number.")

  # Access and print the chosen key's value
  # selected_key = keys[choice - 1]
  # value = data[selected_key]
  # print(f"\nValue of '{selected_key}': {value}")

if __name__ == "__main__":
  print('this runs using cli.py')
#   main()
