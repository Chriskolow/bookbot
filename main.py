from stats import text_to_wordcount
from stats import text_to_charactercount
from stats import sort_charactercount

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {text_to_wordcount(get_book_text("books/frankenstein.txt"))} total words")
    #print(text_to_charactercount(get_book_text("books/frankenstein.txt")))
    sort_characters = sort_charactercount(text_to_charactercount(get_book_text("books/frankenstein.txt")))
    print("--------- Character Count -------")
    for character in sort_characters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")

main()