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

def sort_on(dict):
    return dict["num"]

def sort_char(count_chars):
    sort_list = []
    for char in count_chars:
        count = count_chars[char]
        sort_list.append({"char": char, "num": count})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


    
    