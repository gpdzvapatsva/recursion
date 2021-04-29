
def fib(num):
    if num == 0 :
        return 0
    if num == 1:
        return 1
    else :
            return fib(num-1) +fib(num-2)

num = range(20)
for n in num:
    print(fib(n) , end=" ")
