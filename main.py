def main():
    book_path = "books/frankenstein.txt" #the file path to your desired book or text
    file_text = get_book_text(book_path) #extracts the text from the file using the file path 
    word_count = get_word_count(file_text) #splits the strings in a list and return the length of the list, aka the word count
    character_count = get_text_characters(file_text) #counts every character in the text using a dictionary
    sorted_character_count_list = sort_character_count_list(character_count) #adds the characters to a list for easy sorting using .sort()
    print(f"there are {word_count} words in {book_path}.")
    for item in sorted_character_count_list:
        if not item["character"].isalpha(): #checks if the character is between a-z
            continue
        print(f"The '{item['character']}' character was found {item['total']} times")

def get_book_text(book_path):
    with open("books/frankenstein.txt") as file:
        file_text = file.read()
        return file_text
    
def get_word_count(file_text):
    word_list = file_text.split()
    word_count = len(word_list)
    return word_count

def get_text_characters(file_text): 
    character_count = {}
    for character in file_text: 
        lowered_charcter = character.lower()
        if lowered_charcter in character_count:
            character_count[lowered_charcter] += 1
        else:
            character_count[lowered_charcter] = 1
    return character_count

def get_sort_key(charachter_count):
    return charachter_count["total"]

def sort_character_count_list(character_count):
    sorted_character_count_list = []
    for charachter in character_count:
        sorted_character_count_list.append({"character": charachter, "total": character_count[charachter]})
        sorted_character_count_list.sort(reverse=True, key=get_sort_key)
    return sorted_character_count_list

main()