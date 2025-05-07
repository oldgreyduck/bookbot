from stats import count_words
from stats import count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    num_chars = count_chars(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
