def get_unique_list_numbers(a, b, list_size) -> list[int]:
    from random import randint
    unique = []
    while len(unique) !=list_size:
        for i in range(list_size):
            i = randint(a, b)
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique
    ...  # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers(-10,10,15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
