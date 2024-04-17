import time


# Pierwszy i najprostszy problem w którym, znacząco przyspieszamy algorytm rekurencyjny poprzez spamiętywanie
# wyrazów ciągu, które już raz policzyliśmy dzięki czemu nie musimy ich liczyć na nowo.

def rec_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


def it_fib(n):
    a = 1
    b = 1
    while n - 2 > 0:
        b = a + b
        a = b - a
        n -= 1

    return b


# total_time = 0
# for i in range(2, 42):
#     start_time = time.time()
#     term = rec_fib(i - 1)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     total_time += elapsed_time
#     print(term, round(elapsed_time, 2), "s")
#
# print("Total time needed for recursive:", round(total_time, 2), "seconds\n")

# total_time = 0
# for i in range(1, 20000):
#     start_time = time.time()
#     term = it_fib(i)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     total_time += elapsed_time
#     print(i, round(elapsed_time, 2), "s")
#
# print("Total time needed for iterative:", round(total_time, 2), "seconds")

start_time = time.time()
it_fib(1000000)
end_time = time.time()

print("Total time needed:", round(end_time - start_time), "seconds")
