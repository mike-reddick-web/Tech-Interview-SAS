import os
from datetime import datetime

# Set to store unique, valid date-time values
valid_dates = set()

# Open the input file
try:
    with open(f'{os.getcwd()}\\dates.txt', 'r') as file:
      for line in file:
        date_string = line.strip()
        try:
          #Check if line is iso format from datetime library
          datetime.fromisoformat(date_string)
          valid_dates.add(date_string)
        except ValueError:
          continue
except:
    print("Error: Make sure there is a dates.txt file in this folder.\nThis can be gathered from running date_generation.py")
    exit()
#Open output file to write unique date-time values
with open(f'{os.getcwd()}\\output.txt', 'w') as output_file:
    output_file.write("\n".join(sorted(valid_dates, reverse=True)))

print("Unique valid date-time values have been written to 'output.txt'.")
