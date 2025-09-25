import re, os

# Regex pattern generated with the help of ChatGPT (OpenAI)
#### Prompt: Write a regex match, provide only the match string, that would be iso8601 compliant for YYYY-MM-DDThh:mm:ssTZD, 
#### this includes making sure the months and days are in appropriate ranges as well as timezone and 'Z'. Allow hh 00 through 23, mm 00 through 59, ss 00 through 59.

pattern = re.compile(r'^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])[T ](\d{2}):(\d{2}):(\d{2})(?:\.(\d+))?(Z|([+-])(\d{2}):(\d{2}))?$')

# Set to store unique, valid date-time values
valid_dates = set()

try:
    # Open the input file
    with open(f'{os.getcwd()}\\dates.txt', 'r') as file:
        for line in file:
            date = line.strip()

            if pattern.match(date):  # Check if the date matches the regex
                valid_dates.add(date)
except:
    print("Error: Make sure there is a dates.txt file in this folder.\nThis can be gathered from running date_generation.py")
    exit()

# Open the output file where unique valid date-time values will be written
with open(f'{os.getcwd()}\\output_test.txt', 'w') as output_file:
    output_file.write("\n".join(sorted(valid_dates, reverse=True)))

print("Unique valid date-time values have been written to 'output_test.txt'.")
