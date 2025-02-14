def count_chars(file_contents):
    lower_case = file_contents.lower()
    dict = {}
    for char in lower_case:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def sort_on(my_dict):
    # sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    # sorted_dict = [{"key": key, "value": value} for key, value in dict.items()]
    # print(sorted_dict)
    return my_dict[1]

def report(count, my_dict):
    sorted_list = list(my_dict.items())
    sorted_list.sort(key=sort_on, reverse=True)
    print(sorted_list)
    sorted_dict = dict(sorted_list)
    print(sorted_dict)
    print(dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print(" ")
    for char in sorted_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_dict[char]} times")
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    words = file_contents.split()
    count = len(words)
    # print(count)
    # print(count_chars(file_contents))
    report(count, count_chars(file_contents))


main()
