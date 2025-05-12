import re

field = ['book_name', 'book_author', 'copies_available', 'copies_rented']
def read_library(p):
    bk = None
    with open(f'maintainability_example/{p}', 'r', encoding='utf-8') as file:
        bk = file.readlines()

    if bool(bk):
        for index, book in enumerate(bk):
            if re.search(r'^>', book):
                bf = book[2:].split('; ')
                if len(bf) == 4:
                    rep = '-'*10 + '\n'
                    nok = False
                    for id in range(4):
                        if bool(bf[id]):
                            rep += f'{field[id]}: {bf[id]}\n'
                        else:
                            print(f'line {index+1} has an empty field')
                            nok = True
                    if nok:
                        continue
                    rep += '-'*10
                    print(rep, end='\n\n')   
                else:
                    print(f'line {index+1} has the wrong number of fields')                
            else:
                print(f'line {index+1} is not a book')            
    else:
        raise ValueError('File is empty')
    
while True:
    provided_path = input('Type the file name ("stop" to end): ')

    if provided_path == 'stop':
        break

    try:
        read_library(provided_path)

    except FileNotFoundError as e:
        print(f'You might have passed the wrong file name: {e}')
    
    except ValueError as e:
        print(f'The file might be empty: {e}')

    except Exception as e:
        print(f'Unknown Error: {e}')
        break 