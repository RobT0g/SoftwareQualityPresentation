# I want a code that can count the numbers of book I have read
import re


with open('./functional_example/library_example.txt', 'r') as file:
    library = file.readlines()
    number_of_books = 0

    for line in library:
        if not re.search(r'^-', line):
            continue

        if not re.search(r'by', line):
            continue

        number_of_books += 1

    print(f'I have read {number_of_books} books! Nice!')
