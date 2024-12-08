
a = [42, 69, 322, 13, 99, 0, -5, 9, 8, 7, -6, 5]

i = 0
while i < len(a):
    if a[i] < 0:
        break
    if a[i] != 0:
        print(i, a[i])

        i += 1

