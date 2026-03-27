numbers = {1, 2, 3, 4, 5, 6, 7, 8}

even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

print("Count of even numbers:", even_count)
