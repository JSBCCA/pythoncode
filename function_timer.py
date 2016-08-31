import time
import linearsearch1
import linearsearch2
import linearsearch3


def time_it(search, L, v):
    """(function, list, object) -> number

    Time how long it takes to run function search to find value v in list L.
    """
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0


def print_times(v, L):
    """(object, list) -> NoneType

    Print the number of milliseconds it takes for linear_search(v, L) to run
    for list.index, the while loop linear search, the for loop linear search,
    and sentinel search.
    """
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    while_time = time_it(linearsearch1.linear_search, L, v)
    for_time = time_it(linearsearch2.linear_search, L, v)
    sentinel_time = time_it(linearsearch3.linear_search, L, v)

    print("{0:^10}{1:^10.2f}\t{2:^10.2f}\t{3:^10.2f}\t{4:^10.2f}".format(
        v, while_time, for_time, sentinel_time, index_time))


L = list(range(10000001))

print_times(10, L)
print_times(5000000, L)
print_times(10000000, L)
