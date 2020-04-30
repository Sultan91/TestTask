
'''
Calculates mean, median, min, max values via rolling window method
'''


def mean(arr: list):
    return sum(arr)/len(arr)


def median(arr: list):
    arr = sorted(arr)
    if len(arr) == 1:
        return arr[0]
    if len(arr) % 2 == 0:
        return (arr[(len(arr))//2-1] + arr[(len(arr))//2]) / 2
    else:
        return arr[len(arr)//2]


def statistics(window: list):
    return mean(window), median(window), max(window), min(window)


def task2(dataset, w_size=100):
    res = []
    for i in range(w_size, len(dataset[0])):
        res.append(statistics(dataset[1][i-w_size:i]))
    return list(zip(*res))

