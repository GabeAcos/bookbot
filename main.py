from stats import word_count, character_count, pretty_print_cc
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    dict_char = character_count(book_text)
    sorted_dict_char = pretty_print_cc(dict_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_dict_char:
        print(f"{x['character']}: {x['num']}")
    # print(f"{l["character"]}: {l["num"]}"
    print("============= END ===============")


if __name__ == "__main__":
    main()
