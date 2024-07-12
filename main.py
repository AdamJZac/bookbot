def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_list = dict_to_list(char_count)
    build_report(book_path, word_count, char_list)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lc_text = text.lower()
    output = {}
    for char in lc_text:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    output = []
    for key in dict:
        if key.isalpha():
            output.append({"char": key, "count": dict[key]})
    output.sort(reverse=True, key=sort_on)
    return output

def build_report(path, wc, cc):
    print(f"--- Begin report of {path} ---")
    print(f"{wc} words found in the document")
    print("")

    for entry in cc:
        key = entry["char"]
        value = entry["count"]
        print(f"The '{key}' character was found {value} times")
    
    print(f"--- End report ---")


main ()