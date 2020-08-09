import argparse, pyperclip

# def mock_text(user_text):
#     user_text_list = list(user_text.lower())
#     for i in range(0, len(user_text_list), 2):
#         if not user_text_list[i].isalpha():
#             i -= 1
#         user_text_list[i] = user_text_list[i].upper()
#     return ''.join(user_text_list)

# TODO: Refactor original function to use format_input
def mock_text(user_text):
    pass

def format_input(user_text):
    special_chars = [(index, char) for index, char in enumerate(user_text) if not char.isalpha()]
    user_text_list = [letter for letter in user_text if letter.isalpha()]
    return user_text_list, special_chars

def main():
    # print(mock_text(args.user_text))
    pass

parser = argparse.ArgumentParser(prog='spongemock.py')
parser.add_argument('user_text', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    main()