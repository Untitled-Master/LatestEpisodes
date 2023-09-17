import requests

# Define the API endpoint URL
api_url = 'https://animeapi-1.u1u1u1u1u1u1u1.repl.co/anime_images'

# Send a GET request to the API
response = requests.get(api_url)

# Initialize an empty string to store the names
names_to_print = ""

# Check the response status code
if response.status_code == 200:
  # Parse the JSON response
  data = response.json()

  # Iterate through the list of dictionaries and add names to the variable (excluding specific names)
  for item in data:
    name = item.get('name', 'No Name Available')

    # Check if the name is one of the excluded names
    if name not in [
        "إكس إس أنمي", "أحمد الشيخ | تصيم وبرمجة قوالب ووردبريس وبرمجيات خاصة."
    ]:
      names_to_print += f'Anime: {name}\n ------------\n'

# Print the collected names
print(names_to_print)
