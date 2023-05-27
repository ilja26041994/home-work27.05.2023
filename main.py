# # 6.4
# count = 0
# while True:
#     n = int(input('some negative number '))
#     count += 1
#     if n > 0:
#         break
# print('quantity of negative numbers', count)
# 6.6
cnt = 0
n = int(input('number n'))
while True:
    a = int(input('number a'))
    cnt += 1
    if a < n:
        x1 = 1 * a
        x2 = 1 * cnt
    if a > n and a != n: # неверное условие для определения числа следующего за числом н
        x3 = 1 * a
        x4 = 1 * cnt
    if cnt == 5:
        break
print('summa a < n =', a)
print('the ordinal number of the number', x1, 'this', x2)
print('the ordinal number of the number', x3, 'this', x4)
