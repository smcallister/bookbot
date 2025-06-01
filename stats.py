def get_word_count(text):
    return len(text.split())

def get_count_by_char(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    return chars

def sort_on(dict):
    return dict["num"]

def sort_count_by_char(chars):
    counts = []
    for char in chars:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = chars[char]
        counts.append(char_dict)
    
    counts.sort(reverse=True, key=sort_on)
    return counts