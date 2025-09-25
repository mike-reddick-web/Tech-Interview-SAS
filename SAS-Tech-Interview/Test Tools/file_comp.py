import filecmp, os
try:
    print(filecmp.cmp(f'{os.getcwd()}\\output.txt', f'{os.getcwd()}\\output_test.txt'))
except:
    print("Error: Must run iso8601_format_check.py and regex_chatgpt.py\nin the same folder as file_comp.py before running file_comp.py")