"""
Nathan Gu and Blake Potvin
Sorting Project - Starter
CSE 331 Fall 2023
"""

import random
import time
from typing import TypeVar, List, Callable, Dict, Tuple
from dataclasses import dataclass

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Helper function to determine the order of two elements based on the provided comparator and sorting order.

    Parameters:
    - first: The first element to be compared.
    - second: The second element to be compared.
    - comparator: A function which takes two arguments of type T and returns True when the first argument
                  should be treated as less than the second argument.
    - descending: A boolean indicating whether the list should be sorted in descending order.

    Returns:
    - bool: True if the first element should come before the second element in the sorted list, False otherwise.
    """
    result = comparator(first, second)
    return not result if descending else result


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list of values in-place using the selection sort algorithm and the provided comparator.

    Parameters:
    - data: List of items to be sorted.
    - comparator: A function which takes two arguments of type T and returns True when the first argument
                  should be treated as less than the second argument. Defaults to less than comparison.
    - descending: A boolean indicating whether the list should be sorted in descending order. Defaults to False.

    Returns:
    None. The list is sorted in-place.
    """
    n = len(data)
    for i in range(n):
        # Assume the minimum is the first element
        min_idx = i
        # Test against elements after i to find the smallest
        for j in range(i + 1, n):
            if do_comparison(data[j], data[min_idx], comparator, descending):
                min_idx = j
        # Swap the found minimum element with the first element
        data[i], data[min_idx] = data[min_idx], data[i]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sorts a list of values in-place using the bubble sort algorithm and the provided comparator.

    Parameters:
    - data: List of items to be sorted.
    - comparator: A function which takes two arguments of type T and returns True when the first argument
                  should be treated as less than the second argument. Defaults to less than comparison.
    - descending: A boolean indicating whether the list should be sorted in descending order. Defaults to False.

    Returns:
    None. The list is sorted in-place.
    """
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if do_comparison(data[j + 1], data[j], comparator, descending):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        # If no two elements were swapped by inner loop, then the list is sorted
        if not swapped:
            break


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list of values in-place using the insertion sort algorithm and the provided comparator.

    Parameters:
    - data: List of items to be sorted.
    - comparator: A function which takes two arguments of type T and returns True when the first argument
                  should be treated as less than the second argument. Defaults to less than comparison.
    - descending: A boolean indicating whether the list should be sorted in descending order. Defaults to False.

    Returns:
    None. The list is sorted in-place.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and do_comparison(key, data[j], comparator, descending):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts a list of values using a hybrid merge sort algorithm, which utilizes insertion sort for smaller subarrays.
    
    Parameters:
    - data: List of items to be sorted.
    - threshold: The maximum size of subarray to apply insertion sort to. Defaults to 12.
    - comparator: A function which takes two arguments of type T and returns True when the first argument
                  should be treated as less than the second argument. Defaults to less than comparison.
    - descending: A boolean indicating whether the list should be sorted in descending order. Defaults to False.
    
    Returns:
    None. The list is sorted in-place.
    """
    if len(data) <= 1:
        return

    if len(data) <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
        return

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    hybrid_merge_sort(left_half, threshold=threshold, comparator=comparator, descending=descending)
    hybrid_merge_sort(right_half, threshold=threshold, comparator=comparator, descending=descending)

    # Merging the two halves back into the original data list
    merged = merge(left_half, right_half, comparator=comparator, descending=descending)
    for i, value in enumerate(merged):
        data[i] = value

def merge(left: List[T], right: List[T], *, comparator: Callable[[T, T], bool], descending: bool) -> List[T]:
    """
    Merges two sorted lists into a single, sorted list.
    
    Parameters:
    - left: The first sorted list to be merged.
    - right: The second sorted list to be merged.
    - comparator: A function which takes two arguments of type T and returns True when the first argument
                  should be treated as less than the second argument.
    - descending: A boolean indicating whether the merged list should be in descending order.
    
    Returns:
    - List[T]: A new list containing all elements from 'left' and 'right', sorted according to 'comparator' and 'descending'.
    """
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if do_comparison(left[left_index], right[right_index], comparator, descending):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def maximize_rewards(item_prices: List[int]) -> Tuple[List[Tuple[int, int]], int]:
    """
    Finds pairs of items whose prices sum up to the same value and calculates the total reward.
    
    Parameters:
    - item_prices: A list of integers representing the prices of items.
    
    Returns:
    - Tuple[List[Tuple[int, int]], int]: A tuple where the first element is a list of pairs of items whose prices
                                         sum up to the same value, and the second element is the total reward calculated
                                         as the product of the prices in each pair. If no such pairs are found, returns
                                         an empty list and -1.
    """
    if len(item_prices) % 2 == 1 or not item_prices:
        return ([], -1)

    hybrid_merge_sort(item_prices)

    left, right = 0, len(item_prices) - 1
    target_sum = item_prices[left] + item_prices[right]
    pairs = []

    while left < right:
        current_sum = item_prices[left] + item_prices[right]
        if current_sum == target_sum:
            pairs.append((item_prices[left], item_prices[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    # If we couldn't pair up all items, return -1
    if len(pairs) * 2 != len(item_prices):
        return [], -1

    total = sum(x * y for x, y in pairs)
    return pairs, total



def quicksort(data) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)
