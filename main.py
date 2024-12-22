def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words(file_contents)} words found in the document")
    print_characters_dict(count_chars(file_contents))
    print("--- End report ---")
    
def print_characters_dict(chars):
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times")

def num_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_chars(file_contents):
    words = file_contents.split()
    chars = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

main()