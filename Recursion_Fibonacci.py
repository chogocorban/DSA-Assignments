# for x in range(6):
#   print(x)
#
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n ==2:
#         return 1
#     elif n >2:
#         return fibonacci(n-1) + fibonacci(n - 2)
# for i in range(1,500):
#     print(i, ":",fibonacci(i))
#
# cache = {}
#
# value = 0
#
# def fibonacci2(n):
#
#     if n in cache:
#         return cache[n]
#
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci2(n-1) + fibonacci2(n-2)
#     cache[n] = value
#     return value
#
# for i in range(1,500):
#     print(f"{i} Term: {fibonacci2(i)}")

from functools import lru_cache

#L -> LAST, R-> RECENTLY, C -CACHE
@lru_cache(maxsize=1000)
def fib3(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib3(n-1) + fib3(n-2)
for  i in range(1,1000):
    print(i,":",fib3(i))

