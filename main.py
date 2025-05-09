from stats import count_words
from stats import count_chars
from stats import sort_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    num_chars = count_chars(text)
    char_list = sort_char(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
