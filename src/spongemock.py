def mock_text(user_text):
    user_text_list = list(user_text.lower())
    for i in range(0, len(user_text_list), 2):
        if not user_text_list[i].isalpha():
            i -= 1
        user_text_list[i] = user_text_list[i].upper()
    return ''.join(user_text_list)

mock_text('this is a test')
