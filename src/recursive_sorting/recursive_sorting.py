# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled


# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    #merged_arr = [0] * elements
    merged_arr = []
    left = 0
    right = 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    while left < len(arrA):
        merged_arr.append(arrA[left])
        left += 1
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1

    # TO-DO
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    lhs = arr[:middle]
    rhs = arr[middle:]
    return merge(merge_sort(lhs), merge_sort(rhs))

list1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
list2 = merge_sort(list1)
print(list2)


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr
#
#
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr
#
#
# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     return arr
