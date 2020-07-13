def mock_text(user_text):
    user_text_list = list(user_text.lower())
    for i in range(0, len(user_text_list), 2):
        if not user_text_list[i].isalpha():
            i -= 1
        user_text_list[i] = user_text_list[i].upper()
    return ''.join(user_text_list)

def format_input(user_text):
    special_chars = [(index, char) for index, char in enumerate(user_text) if not char.isalpha()]

# def main():
#     user_text = input("Enter text to mock: ")
#     mock_text(user_text)

# if __name__ == "__main__":
#     main()
