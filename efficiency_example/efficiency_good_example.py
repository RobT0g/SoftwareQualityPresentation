import time

numbers = None
with open('./efficiency_example/numbers.txt', 'r') as file:
    numbers = [int(i) for i in file.readlines()[0].split(', ')]

start = time.perf_counter()
ordered_numbers = numbers.sort()
end = time.perf_counter()

print(f"Elapsed time: {end - start:.6f} seconds")
