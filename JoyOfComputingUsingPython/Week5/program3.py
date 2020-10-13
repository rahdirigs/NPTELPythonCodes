n = int(input())


def printDict():
    my_dict = dict()
    for i in range(1, n + 1):
        my_dict[i] = i ** 2
    print(my_dict)


printDict()
