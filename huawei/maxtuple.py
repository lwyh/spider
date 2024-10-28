import functools

arr = input().split(",")
print(arr)

def cmp(a,b):
    s1 = a+b
    s2 = b+a
    return 0 if s1 == s2 else -1 if s1>s2 else 1
def result():
    arr.sort(key=functools.cmp_to_key(cmp))
    return "".join(arr)
print(result())

