data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_):
    # Проверяем является ли аргумент простым значением, для int, float, bool - возвращаем значение аргумента,
    # для str - длину строки
    if isinstance(data_, bool):
        return int(data_)
    elif isinstance(data_, int) or isinstance(data_, float):
        return data_
    elif isinstance(data_, str):
        return len(data_)
    elif isinstance(data_, dict):  # если аргумент является словарь - преобразуем все ключи и значения в обычный список
        return calculate_structure_sum(list(data_.values()) + list(data_.keys()))
    else:  # Если же аргумент является одномерной коллекцией (list, tuple, set) - то перебираем все элементы коллекции
        sum = 0
        for item in data_:
            if isinstance(item, int) or isinstance(item, float) or isinstance(item, bool):
                sum += item
            elif isinstance(item, str):
                sum += len(item)
            elif isinstance(item, dict):
                sum += calculate_structure_sum(list(item.values()) + list(item.keys()))
            else:
                sum += calculate_structure_sum(item)
        return sum


result = calculate_structure_sum(data_structure)
print(result)

# check result for some types of data_structures

data_structure = 'simple text'
print(calculate_structure_sum(data_structure))

data_structure = 36.6
print(calculate_structure_sum(data_structure))

data_structure = True
print(calculate_structure_sum(data_structure))

data_structure = {5, 10, 'Hello', (1, 2, 3), (4, 5, 6), (7, 8, 9)}
print(calculate_structure_sum(data_structure))

data_structure = {1: "Apple", 2: "Banana", 3: "Cherry"}
print(calculate_structure_sum(data_structure))
