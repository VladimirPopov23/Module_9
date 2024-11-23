# module_9_6.py
# 24.11.2024 Домашнее задание по теме "Генераторы"

def all_variants(text):
    for j in range(1, len(text) + 1):
        for y in range(len(text) - j + 1):
            yield text[y: y + j]


a = all_variants("abc")
for i in a:
    print(i)
