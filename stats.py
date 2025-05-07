def count_words(text):
    return len(text.split())

def count_chars(text):
    lower_case = text.lower()
    unique_chars = {}
    for char in lower_case:
        if char in unique_chars:
            unique_chars[char] = unique_chars[char] + 1
        else: unique_chars[char] = 1
    return unique_chars
