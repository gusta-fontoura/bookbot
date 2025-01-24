def count_words(file_contents):
    result = {}
    for letter in file_contents.lower():
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def print_report(result, total):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} words found in the document")

    sorted_result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_result)
    
    for letter in converted_dict:
        if letter.isalpha():
            number = converted_dict[letter]
            print(f"The '{letter}' character was found {number} times")



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total = len(file_contents.split())
        print(f"total = {total}")
        result = count_words(file_contents)
        print_report(result, total)


main()
