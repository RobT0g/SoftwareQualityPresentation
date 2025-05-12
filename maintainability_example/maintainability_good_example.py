import re

fields_assignment = ['book_name', 'book_author', 'copies_available', 'copies_rented']
def read_library(path_to_file:str):
    ''' PEP 257 Format
    This function reads a txt file and tries to interpret it as collection of books

    Each line should be a book and contain the following structure:
    > Book Name; Book Author; Number of copies available; Number of copies rented

    Args:
        path_to_file (str): The path to the file specified
    
    Returns:
        None

    Raises:
        FileNotFoundError: If the specified path does not exist
        ValueError: If the file exists but is empty
    '''

    library_file = None
    with open(f'maintainability_example/{path_to_file}', 'r', encoding='utf-8') as file:
        library_file = file.readlines()

    if not bool(library_file):
        raise ValueError('File is empty')
    
    for index, book in enumerate(library_file):
        if not re.search(r'^>', book):
            print(f'line {index+1} is not a book')
            continue

        book_fields = book[2:].split('; ')
        if not len(book_fields) == 4:
            print(f'line {index+1} has the wrong number of fields')

        book_report = '-'*10 + '\n'
        line_not_ok = False
        for field_index in range(4):
            if not bool(book_fields[field_index]):
                print(f'line {index+1} has an empty field')
                line_not_ok = True
                break

            book_report += f'{fields_assignment[field_index]}: {book_fields[field_index]}\n'
        
        if line_not_ok:
            continue

        book_report += '-'*10
        print(book_report, end='\n\n')


while True:
    provided_path = input('Type the file name ("stop" to end): ')

    if provided_path == 'stop':
        break

    try:
        read_library(provided_path)

    # Reliability Example
    except FileNotFoundError as e:
        print(f'You might have passed the wrong file name: {e}')
    
    except ValueError as e:
        print(f'The file might be empty: {e}')

    except Exception as e:
        print(f'Unknown Error: {e}')
        break 