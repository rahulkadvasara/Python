import multiprocessing
from multiprocessing import Pool


# # processing numbers 

# def f(n):
#     return n*n

# if __name__ == "__main__":
#     p = Pool(processes=3)
#     result = p.map(f,[1,2,3,4,5])
#     for n in result:
#         print(n)


# # without processing numbers

# def f(n):
#     return n*n

# if __name__ == "__main__":
#     p = Pool()
#     result = p.map(f,[1,2,3,4,5])
#     print(result)
#     p.close()
#     p.join()


# time example

import time
def f(n):
    sum=0
    for x in range(1000):
        sum+=x*x
    return sum

if __name__=="__main__":
    t1=time.time()
    p=Pool()
    result=p.map(f,range(100000))
    p.close()
    p.join()

    print("Pool took : ",time.time()-t1)

    t2=time.time()
    result=[]
    for x in range(100000):
        result.append(f(x))

    print("Serial process took : ",time.time()-t2)

