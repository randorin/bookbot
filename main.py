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
            result_dict = dict(char_count)
        print(result_dict)
main()
count_words("books/frankenstein.txt")
count_chars("books/frankenstein.txt")