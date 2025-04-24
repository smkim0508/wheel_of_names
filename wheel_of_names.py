import os
import random

# set folder path as current directory
folder_path = './'
delimiter = '\n'

# list to hold split values
names = []

# loop through all txt files in the folder
for filename in os.listdir(folder_path):
   if filename.endswith('.txt'): # could be changed to be more specific
      file_path = os.path.join(folder_path, filename)
      with open(file_path, 'r', encoding='utf-8') as file:
         content = file.read()
         # split the file content using delimiter
         parts = content.split(delimiter)
         names.append(parts)

# function to return n random items from data list
def select_random_items(data, n):
    if n > len(data):
        raise ValueError("please enter a smaller value!")
    return random.sample(data, n)

number_people = int(input())

selected_items = select_random_items(names[0], number_people)

for item in selected_items:
   print(item)