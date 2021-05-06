import time
for i in range(101):
    a='#'*i
    b='*'*(100-i)
    c=(i/100)*100
    print("\r|{}{}|{:.2f}%".format(a,b,c),end='')
    time.sleep(0.1)
