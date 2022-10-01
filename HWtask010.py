# Реализуйте алгоритм перемешивания списка

import random


sizelist = int(input('Введите размер списка: '))
somelist = []
for i in range(sizelist):
    somelist.append(i)
print(somelist)
stepofmix = 1000
for i in range(stepofmix):
    a = round(random.random()*(sizelist-1))
    b = round(random.random()*(sizelist-1))
    (somelist[a], somelist[b])=(somelist[b], somelist[a])
print(somelist)

# Простой способ
# random.shuffle(somelist)
# print(somelist)
