# bubble-sort
#
import random

random_list = [random.randint(1, 10) for i in range(10)]


def bubble_sort(unsorted_list: list) -> list:
    for i_first, num in enumerate(unsorted_list):
        second_list = random_list
        if i_first != 0:
            second_list = unsorted_list[:-i_first:]
        for i_second, number in enumerate(second_list[:-1:]):
            if unsorted_list[i_second] > unsorted_list[i_second + 1]:
                unsorted_list[i_second], unsorted_list[i_second + 1] = unsorted_list[i_second + 1], unsorted_list[
                    i_second]
    return unsorted_list


def bubble_sort1(unsorted_list: list) -> list:
    for i in range(0, len(unsorted_list), 1):
        for j in range(0, len(unsorted_list) - i - 1, 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


def bubble_sort2(unsorted_list: list) -> list:
    ul = unsorted_list
    for i in range(len(ul)):
        for j in range(len(ul)-i-1):
            if ul[j] > ul[j+1]:
                ul[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return ul


print(bubble_sort(random_list))
print(bubble_sort1(random_list))
print(bubble_sort2(random_list))
