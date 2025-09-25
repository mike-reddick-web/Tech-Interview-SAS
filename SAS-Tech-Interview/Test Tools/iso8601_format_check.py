import os
from datetime import datetime

# Set to store unique, valid date-time values
valid_dates = set()

# Open the input file
retry = 0
while retry<=1:
    try:
        with open(f'{os.getcwd()}\\dates.txt', 'r') as file:
          for line in file:
            date_string = line.strip()
            try:
              #Check if line is iso format from datetime library
              if('+' in date_string[-6:] or  '-' in date_string[-6:] or 'Z' in date_string[-1]):	
                datetime.fromisoformat(date_string)	      
                valid_dates.add(date_string)
            except ValueError:
              continue
        retry+=1
    except:
	
        if retry == 1:
             print("Error: No file dates.txt. Unable to generate.\nPlease move date_generator.py from Test Tools to this working directory. Alternatively, provide a 'dates.txt' file.")
             exit()
        print("Error: No file 'dates.txt'. Attempting to generate...")
        retry+=1
        try:
            import date_generator
        except:
            continue
        continue

#Open output file to write unique date-time values
with open(f'{os.getcwd()}\\output.txt', 'w') as output_file:
    output_file.write("\n".join(sorted(valid_dates, reverse=True)))

print("Unique valid date-time values have been written to 'output.txt'.")


