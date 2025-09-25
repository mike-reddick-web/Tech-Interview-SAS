Run date_generator -> (iso88601_format_check/regex_chatgpt) -> file_comp

python date_generator.py
	-Will generate 1.5 million random dates (possibly some duplicates, intentional)
	-Will copy .5 million random dates, to be ignored per the instructions
	-Will copy .5 million random dates, change the hyphens to backslashes, thus not making them iso compliant

	Outputs to dates.txt

python iso8601_format_check.py or regex_chatgpt.py
	-Will add unique dates to a set, thus avoiding duplicates
	-Outputs to output.txt and output_test.txt respectively

python file_comp.py
	-Prints true/false if regex and iso output files are equal