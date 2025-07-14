def text_to_wordcount(text):
    words = text.split()
    return len(words)

def text_to_charactercount(text):
    letters = {}
    for letter in text:
        if letter.lower() in letters:
            letters[letter.lower()] += 1
        else:
            letters[letter.lower()] = 1
    return letters