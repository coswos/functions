num = 50
print('for ->')
for i in range(1, num):
    if i ** 2 > num:
        break
    print(i ** 2, end=" ")

i = 1
print('\nwhile ->')

while i ** 2 < num:
    print(i ** 2, end=' ')
    i += 1

print('\nfor_2 ->')
for i in range(1, num):
    if i ** 2 < num:
        print(i ** 2, end=' ')
    else:
        break
        