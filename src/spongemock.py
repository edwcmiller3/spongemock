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
    # fuck with chars here
    # then combine into a string
    # ''.join([i[1] for i in sorted(chars + special)])
    pass

def enum_non_alpha(user_text):
    return [(index, char) for index, char in enumerate(user_text) if not char.isalpha()]

def enum_alpha(user_text):
    return [(index, char) for index, char in enumerate(user_text) if char.isalpha()]

def main():
    print(mock_text(args.user_text))
    pass

parser = argparse.ArgumentParser(prog='spongemock.py')
parser.add_argument('user_text', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    main()