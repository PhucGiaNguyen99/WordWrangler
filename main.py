# Functions to manipulate ordered word lists

def remove_duplicates(list1) -> list:
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    unique_list = []
    for num in list1:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersection_list = []
    if len(list1) <= len(list2):
        for num in list1:
            if num in list2:
                intersection_list.append(num)
    else:
        for num in list2:
            if num in list1:
                intersection_list.append(num)
    return intersection_list


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    list1_copy = []
    list2_copy = []

    for idx in range(len(list1)):
        list1_copy.append(list1[idx])
    for idy in range(len(list2)):
        list2_copy.append(list2[idy])

    merge_list = []

    # loop until we reach either the end of list 1 or list 2
    # picking larger elements between two to put in the result list
    while list1_copy and list2_copy:
        if list1_copy[0] < list2_copy[0]:
            merge_list.append(list1_copy.pop(0))
        else:
            merge_list.append(list2_copy.pop(0))
    return merge_list + list1_copy + list2_copy


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """

    # Base case:
    if len(list1) <= 1:
        return list1
    mid_index = len(list1) // 2
    first_half = list1[:mid_index]
    second_half = list1[mid_index:]
    sorted_first = merge_sort(first_half)
    sorted_second = merge_sort(second_half)
    result = merge(sorted_first, sorted_second)
    return result


# Function to generate all strings for the word wrangler game


def print_half(large_list):
    mid_index = len(large_list) // 2
    first_half = large_list[:mid_index]
    second_half = large_list[mid_index:]
    print("First half: ", first_half)
    print("Second half: ", second_half)


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


# def run():
#   """
#  Run game.
# """
# words = load_words(WORDFILE)
# wrangler = provided.WordWrangler(words, remove_duplicates,
#                                intersect, merge_sort,
#                                gen_all_strings)
# provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

if __name__ == '__main__':
    given_list = [3, 5, 1, 8, 4]
    print(merge_sort([1, 4, 2, 3]))
