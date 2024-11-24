# module_9_7.py
# 24.11.2024 Задание: Декораторы в Python

def is_prime(func):
    def wrapper(*args):
        res = func(*args)
# для проверки на простоту необходимо убедится что число больше 0 и не делится ни на что, кроме 1 и самого себя
        if res > 1:
            for j in range(2, res): # в диапазоне от 2 до числа (не включительно)
                if res % j == 0: # если остаток от деления числа не равен 0, то число составное
                    print('Составное')
                    break
            else: # иначе число простое
                print('Простое')
        return res  # возвращаем значение из ф-ции sum_three
    return wrapper  # возвращаем wrapper

@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c # сумма передаваемых чисел
    return sum_

result = sum_three(0, 1, 1)
print(result)
result = sum_three(1, 1, 1)
print(result)
result = sum_three(1, 2, 1)
print(result)
result = sum_three(1, 2, 2)
print(result)
result = sum_three(1, 2, 3)
print(result)
result = sum_three(1, 2, 4)
print(result)
result = sum_three(1, 2, 5)
print(result)
result = sum_three(1, 2, 6)
print(result)
result = sum_three(1, 2, 7)
print(result)
result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 4, 6)
print(result)

