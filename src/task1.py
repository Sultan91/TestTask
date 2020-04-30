import random


def task1(list, k):
    '''
    Chooses random k unique elements from given list
    :var result - is chosen to be a set datatype since we use operation 'in' which is faster
    :param list: list
    :param k: number of items to choose
    :return: chosen random unique numbers
    '''
    result = set([])
    while len(result) < k:
        temp = random.choice(list)
        if temp not in result:
            result.add(temp)
    return result



