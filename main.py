# read text from file and print to screen
def main():
    global book_path
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(path):
    with open(path) as f:
        word_count = 0
        for line in f:
            letter = line.rstrip()
            words = letter.split()
            word_count += len(words)
        print(word_count)

def count_chars(path):
    from collections import Counter
    
    char_count = Counter()

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for char in line:
                lower_char = char.lower()
                if lower_char in char_count:
                    char_count[lower_char] += 1
                else:
                    char_count[lower_char] = 1
            global char_dict
            char_dict = dict(char_count)
        print(char_dict)

def sort_on():
    for key in char_dict:
        if key.isalpha():
            sorted(key)
            print (f"The character: {color.BOLD} {key} {color.END} was found {color.BOLD} {char_dict[key]} {color.END} times.")

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

main()
count_words("books/frankenstein.txt")
count_chars("books/frankenstein.txt")
sort_on()