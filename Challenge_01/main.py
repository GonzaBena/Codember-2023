import requests
URL = "https://codember.dev/data/message_01.txt"

palabras = {}

# Get the data from the URL
result = requests.get(URL)
data = result.text.lower().replace("\n", " ")

# Split the data into words
words = data.split()

# Count the words
for i in words:
    if i in palabras:
        palabras[i] += 1
    else:
        palabras[i] = 1

# Print the result
for i in palabras:
    print(f"{i}{palabras[i]}", end="")
print("\n")