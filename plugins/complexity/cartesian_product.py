#!/usr/bin/python
# Cartesian product (i.e., the number of possible combinations)
import itertools

def cartesian_product(lists):
    """returns the possible combinations"""
    return list(itertools.product(*lists))

# Example usage:
# lists = [[1, 2], ['a', 'b'], [True, False]]
# result = cartesian_product(lists)
# print(result)

def cartesian_product_count(lists):
    """returns the count of possible combinations"""
    count = 1
    for lst in lists:
        count *= len(lst)
    return count

# this breaks click a command disappears
# import numpy as np
# import pandas as pd


# def count_combinations(lists):
#     """Counts the total number of combinations from a list of lists.

#     Args:
#       lists: A list of lists, where each inner list represents a set of options.

#     Returns:
#       The total number of combinations.
#     """

#     if not lists:
#         return 0

#     if len(lists) == 1:
#         return len(lists[0])

#     first_list = lists[0]
#     rest_lists = lists[1:]

#     total_combinations = 0
#     for item in first_list:
#         total_combinations += count_combinations(rest_lists)

#     return total_combinations


# # Example usage:
# # lists = [[1, 2], ["a", "b", "c"], [True, False]]

# # result = count_combinations(lists)
# # print(result)  # Output: 12


# def generate_paths(lists):
#     """Generates all possible paths from a list of lists.

#     Args:
#       lists: A list of lists, where each inner list represents a set of options.

#     Returns:
#       A list of strings, each representing a full path.
#     """

#     if not lists:
#         return []

#     if len(lists) == 1:
#         return [str(item) for item in lists[0]]

#     paths = []
#     for item in lists[0]:
#         for path in generate_paths(lists[1:]):
#             paths.append(str(item) + " -> " + path)

#     return paths
