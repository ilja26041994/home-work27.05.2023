# # 6.4
# count = 0
# while True:
#     n = int(input('some negative number '))
#     count += 1
#     if n > 0:
#         break
# print('quantity of negative numbers', count)
# # 6.6
# v = 1
# b = 1
# cnt = 0
# n = int(input('number n'))
# while True:
#     a = int(input('number a'))
#     cnt += 1
#     if a < n:
#         x1 = 1 * a
#         x2 = 1 * cnt
#     elif cnt == x1 + 1:
#         v *= a
#         b *= cnt
#     if cnt == 15:
#         break
# result = v - x1
# print('summa a < n =', a)
# print('the ordinal number of the number', x1)
# print('this', x2)
# print('the ordinal number of the number', v)
# print('this', b)
# print('разность меньшего от большего', result)
#6.42 a
number = int(input('Input number: '))
maxNumber = 0
maxNumber2 = 9
cnt = 0
cnt2 = 0
while number > 0:
   num = number % 10
   num2 = number % 10
   if num > maxNumber:
       maxNumber = num
       cnt += 1
   if num2 == maxNumber - 1:
       maxNumber2 = num2
       cnt2 += 1
   number = number // 10
print('max =', maxNumber)
print('nomer', cnt)
print('max =', maxNumber2)
print('nomer', cnt2)