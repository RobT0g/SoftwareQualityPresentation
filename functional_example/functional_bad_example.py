# I want a code that can count the numbers of book I have read
# This code breaks if I add a new line or comment in the library

with open('./functional_example/library_example.txt', 'r') as file:
    number_of_books = len(file.readlines())-2

    print(f'I have read {number_of_books} books! Nice!')
