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

def myFunc(e):
  return e['num']

def sort_charactercount(letters):
    letter_list = []
    for letter in letters:
        temp_dic = {"char" : letter, "num" : letters[letter]}
        letter_list.append(temp_dic)
    letter_list.sort(key=myFunc, reverse=True)
    return letter_list