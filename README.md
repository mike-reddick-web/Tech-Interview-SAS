# Tech-Interview-SAS
Python scripts for ISO 8601 date validation

  ## In SAS-Tech-Interview Working Directory

    python iso8601_format_check.py

   This will run all necessary components to generate roughly 2 million date times from date_generator.py and save them to 'dates.txt'. 
   Alternatively, you are able to provide your own list of valid/invalid ISO 8601 date times in a file labeled 'dates.txt'.
   Either way, this script will then produce an output file labeled 'output.txt'. This file will be unique ISO 8601 compliant date times from the datetime Python library. Last minute change - assuming timezone is necessary.

    python date generator.py

  More information on this script - it will generate 2 million dates. 1.5 million ISO 8601 compliant dates. Then 250,000 are copied to another list, and another 250,000 will be copied with slashes instead of hyphens.
  This is to ensure the iso8601_format_check.py script will only accept unique, compliant, and reasonable dates in the 'output.txt' file.



## In Test Tools Working Direcotry

    python file_comp.py

  Running file_comp.py will run all necessary files, including a copy of date_generator, and iso8601_format_ckeck to be in the current working directory. It will also compare the 'output-test.txt' file from regex_chatgpt.py against 'output.txt' from iso8601_format_ckeck. It will then display true or false depending on the outcome (should always be true).

    python regex_chatgpt.py

regex_chatgpt - logically runs similarly to iso8601_format_check, however it uses regex to match the ISO standard instead of the built in Python libraries. This was built as a tool (and partially for fun) using ChatGPT to see if a prompt could be made that returns this exact use case. So far in my testing it has been spot on with all of the dates I've tried. Last minute change - assuming timezone is necessary.

  
