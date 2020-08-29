# -- coding:UTF-8
#!/usr/bin
from cal_time import *


def fibnacci(n):
    if n == 0 or n == 1 :
        return 1
    return fibnacci(n-1) + fibnacci(n-2)

def fibnacci2(n):
    li = [1, 1]
    for i in range(2, n+1):
        li.append(li[-1] + li[-2])
    return li[n]

def fibnacci3(n):
    a = 1
    b = 1
    c = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c

@cal_time
def fib1(n):
    print(fibnacci(n))

@cal_time
def fib2(n):
    print(fibnacci(n))

@cal_time
def fib3(n):
    print(fibnacci(n))

fib1(35)
fib2(35)
fib3(35)

# Steps
# step 1: 把n-1个盘子从A经过C移动到B
# step 2: 把第n个盘子从A移动到C
# step 3: 把n-1个盘子从B经过A移动到C

def hanoi(n, from_pole, through_pole, to_pole):
    if n > 0:
        hanoi(n-1, from_pole, to_pole, through_pole)
        print('%s->%s' % (from_pole, to_pole))
        hanoi(n-1, through_pole, from_pole, to_pole)


hanoi(4, 'A', 'B', 'C')
