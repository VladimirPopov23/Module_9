# module_9_1.py
# 20.11.2024 Задача "Вызов разом"


def apply_all_func(int_list, *functions):
    results = {}

    for i in functions:
        results[i.__name__] = i(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
