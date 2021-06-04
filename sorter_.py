a = [1,3, 8, 6]
b = [2, 7, 4, 9, 5]

def sort(a, b):
    a.extend(b)
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x] < a[y]:
                a[x], a[y] = a[y], a[x]
    return a


print(sort(a,b))

