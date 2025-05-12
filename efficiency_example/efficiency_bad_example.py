import time

numbers = None
with open('./efficiency_example/numbers.txt', 'r') as file:
    numbers = [int(i) for i in file.readlines()[0].split(', ')]

def sorting_function(list_of_numbers: list) -> list:
    ordered_list = []
    
    for number in list_of_numbers:
        insert_at = 0

        for list_item in ordered_list:
            if number < list_item:
                break

            insert_at += 1
        
        ordered_list.insert(insert_at, number)
    
    return ordered_list

start = time.perf_counter()
ordered_numbers = sorting_function(numbers)
end = time.perf_counter()

print(f"Elapsed time: {end - start:.6f} seconds")
