a = int(input())

if a%2 == 0:
    b = a-1
    c = a+2
else:
    b = a-2
    c = a+1

print(f'{b} {c}')