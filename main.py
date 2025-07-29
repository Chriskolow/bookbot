import sys
from stats import text_to_wordcount
from stats import text_to_charactercount
from stats import sort_charactercount

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {text_to_wordcount(get_book_text(sys.argv[1]))} total words")
        #print(text_to_charactercount(get_book_text("books/frankenstein.txt")))
        sort_characters = sort_charactercount(text_to_charactercount(get_book_text(sys.argv[1])))
        print("--------- Character Count -------")
        for character in sort_characters:
            if character["char"].isalpha():
                print(f"{character["char"]}: {character["num"]}")

main()