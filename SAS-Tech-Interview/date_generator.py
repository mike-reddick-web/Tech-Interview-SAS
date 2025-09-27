import random
import datetime

# Function to generate random date created with ChatGPT.
#### Prompt: write random iso date generator +/- or z with list comprehension in python
def generate_random_iso_date():
    # Randomly generate the year, month, day, hour, minute, second
    year = random.randint(1900, 2100)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Keep the day within 1-28 to avoid invalid dates

    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    # Randomly decide to append timezone offset or Z
    add_timezone = random.choice([True, False])  # Choose to add a timezone or Z

    if add_timezone:
        use_offset = random.choice([True, False])  # Randomly choose between offset or Z
        if use_offset:
            sign = random.choice(['+', '-'])
            offset_hour = random.randint(0, 14)  # Timezone offset range: -12 to +14
            offset_minute = random.choice([0, 30])  # Either 00 or 30 minutes
            timezone_offset = f"{sign}{offset_hour:02}:{offset_minute:02}"
            return f"{year}-{month:02}-{day:02}T{hour:02}:{minute:02}:{second:02}{timezone_offset}"
        else:
            return f"{year}-{month:02}-{day:02}T{hour:02}:{minute:02}:{second:02}Z"
    else:
        return f"{year}-{month:02}-{day:02}T{hour:02}:{minute:02}:{second:02}"


def create_file():
  #Generate random dates, duplicate dates (to be ignored), and invalid dates
  random_iso_dates = [generate_random_iso_date() for _ in range(1500000)]
  duplicate_dates = random.choices(random_iso_dates, k=250001)
  invalid_dates = [item.replace('-', '/') for item in random.choices(random_iso_dates, k=250001)]

  # Write the generated random dates to 'dates.txt'
  with open("dates.txt", "w") as file:
    file.write("\n".join(random_iso_dates))
    file.write("\n".join(duplicate_dates))
    file.write("\n".join(invalid_dates))

  print("1.5 million random ISO dates, .5 million duplicates, and .5 million invalid dates written to 'dates.txt'.")

if __name__ == "__main__":
  create_file()

