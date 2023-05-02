def drawing_title(text, fill_with_text, len_string, fill_bord):
    text = ' ' + text + ' '
    clean_len = int((len_string - len(text)) / 2)  # how many need to add symbols
    right_len = len_string - (clean_len + len(text))
    if clean_len != right_len:
        right_len = clean_len
    result_string = (clean_len * fill_with_text) + text + (right_len * fill_with_text)
    len_border = len(result_string)

    print()
    print('len new:', len(text))
    print('len_string:', len_string)
    print('clean_len:', clean_len)
    print('right_len:', right_len)
    print()
    print(len_border * fill_bord)
    print(result_string)
    print(len_border * fill_bord)


drawing_title('hello', '*', 31, '-')
drawing_title('hello', '*', 32, '-')
drawing_title('hello', '*', 33, '-')

