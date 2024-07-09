# Решаем через список. Данный метод точнее решает условие задачи, поскольку не исключает нули (то есть если в числе
# встречается цифра 0, то происходит умножение на 0)
def get_multiplied_digits_list(number):
    list_of_digits = list(str(number))
    if len(list_of_digits) != 1:  # если осталось больше одной цифры - уходим в рекурсию, иначе возвращаем эту цифру
        return int(list_of_digits.pop()) * get_multiplied_digits_list(int("".join(list_of_digits)))
    else:
        return int(list_of_digits.pop())


# Решаем через строку (если в числе есть цифра 0 - то она игнорируется, т.е. умножение на 0 не происходит).
# Это связанно с особенностью выполнения функции int() в результате которой нуль, если он есть в начале строки
# игнорируется
def get_multiplied_digits_str(number):
    string_of_digits = str(number)
    if len(string_of_digits) != 1:  # если осталось больше одной цифры - уходим в рекурсию, иначе возвращаем эту цифру
        return int(string_of_digits[0]) * get_multiplied_digits_str(int(string_of_digits[1:]))
    else:
        return int(string_of_digits[0])


# Решаем через строку, исправляя ошибку 0.
def get_multiplied_digits_str_correct(number):
    string_of_digits = str(number)
    if len(string_of_digits) != 1:  # если осталось больше одной цифры - уходим в рекурсию, иначе возвращаем эту цифру
        return int(string_of_digits[-1]) * get_multiplied_digits_str(int(string_of_digits[:-1]))
    else:
        return int(string_of_digits[0])


print(get_multiplied_digits_list(40203))

print(get_multiplied_digits_str(40203))

print(get_multiplied_digits_str_correct(40203))




