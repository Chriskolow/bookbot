from stats import text_to_wordcount
from stats import text_to_charactercount

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    print(f"{text_to_wordcount(get_book_text("books/frankenstein.txt"))} words found in the document")
    print(text_to_charactercount(get_book_text("books/frankenstein.txt")))

main()