arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            print(smallest_index, 'jiji')
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        # TO-DO: swap

    return arr

selection_sort(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while swaps_have_occurred:
        # set the swaps occured to false
        swaps_have_occurred = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_have_occurred = True

    return arr
#
#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr

