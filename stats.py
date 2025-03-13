def word_count(book_text):
    words = book_text.split()
    return len(words)


def character_count(book_text):
    char_dict = {}
    for c in book_text.lower():
        if not c.isspace():
            char_dict[c] = char_dict.get(c, 0) + 1
    return char_dict


def pretty_print_cc(char_dict):
    list_of_dicts = []
    for k, v in char_dict.items():
        list_of_dicts.append({"character": k, "num": v})
    list_of_dicts = sorted(list_of_dicts, reverse=True, key=lambda d: d["num"])
    return list_of_dicts
