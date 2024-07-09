def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = ["1", True, (1, 2, 3)]
values_dict = {"a": 156, "b": "String", "c": [1, 2, 3]}
print_params(*value_list)
print_params(**values_dict)

value_list2 = [54.32, "Строка"]
print_params(*value_list2)
print_params(*value_list2, 42)
