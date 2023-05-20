import numpy as np

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

# def find_combination(choices, total):
#     """
#     choices: a non-empty list of ints
#     total: a positive int
 
#     Returns result, a numpy.array of length len(choices) 
#     such that
#         * each element of result is 0 or 1
#         * sum(result*choices) == total
#         * sum(result) is as small as possible
#     In case of ties, returns any result that works.
#     If there is no result that gives the exact total, 
#     pick the one that gives sum(result*choices) closest 
#     to total without going over.
#     """
#     # create array of zeros of length len(choices)

#     result = [0] * len(choices)
#     # sort the choices and save in sorted_choices in reverse order
#     sorted_choices = sorted(choices, reverse=True)
#     # for each choice in sorted_choices
#     for choice in sorted_choices:
#         # find pick of choice in choices
#         pick = choices.index(choice)
#         # if choice is less than or equal to total
#         if choice <= total:
#             # set result[pick] to 1
#             result[pick] = 1
#             # clear choice from choices
#             choices[pick] = 0
#             # subtract choice from total
#             total -= choice
#     # return result
#     return np.array(result)

# def find_combination(choices, total):
#     """
#     choices: a non-empty list of ints
#     total: a positive int
 
#     Returns result, a numpy.array of length len(choices) 
#     such that
#         * each element of result is 0 or 1
#         * sum(result*choices) == total
#         * sum(result) is as small as possible
#     In case of ties, returns any result that works.
#     If there is no result that gives the exact total, 
#     pick the one that gives sum(result*choices) closest 
#     to total without going over.
#     """
#     num_choices = len(choices)
#     best_result = None
#     closest_sum = float('-inf')

#     for i in range(2 ** num_choices):
#         result = np.zeros(num_choices, dtype=int)
#         for j in range(num_choices):
#             if (i >> j) & 1:
#                 result[j] = 1

#         sum_product = np.sum(result * choices)
#         sum_choices = np.sum(result)

#         if sum_product == total:
#             return result
#         elif sum_product <= total and sum_product > closest_sum:
#             best_result = result
#             closest_sum = sum_product

#     return np.array(best_result)


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    num_choices = len(choices)
    best_result = None
    closest_sum = float('-inf')

    for i in range(2 ** num_choices):
        result = np.zeros(num_choices, dtype=int)
        for j in range(num_choices):
            if (i >> j) & 1:
                result[j] = 1

        sum_product = np.sum(result * choices)
        sum_choices = np.sum(result)

        if sum_product == total and sum_choices == 1:
            return result
        elif sum_product <= total and sum_product > closest_sum:
            best_result = result
            closest_sum = sum_product

    return np.array(best_result)
        

print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3], 5))
print(find_combination([1,1,1,9], 4))
