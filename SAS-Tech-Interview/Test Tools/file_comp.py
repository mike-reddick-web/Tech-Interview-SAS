import filecmp, os
try:
    print(filecmp.cmp(f'{os.getcwd()}\\output.txt', f'{os.getcwd()}\\output_test.txt'))
except:
    import iso8601_format_check
    import regex_chatgpt
    print(filecmp.cmp(f'{os.getcwd()}\\output.txt', f'{os.getcwd()}\\output_test.txt'))