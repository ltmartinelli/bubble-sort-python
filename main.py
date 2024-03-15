arr = [4,3,2,1]


def bubble_sort(arr):
    # 1 - Initialize sorted flag as False
    sorted = False

    # 2 - Make it run while it's unsorted
    while sorted == False:

        # 3 - Set flag to True. If no swaps are made, it's sorted, so terminate early
        sorted = True

        # 4 - Iterate through the array
        for i in range(len(arr) - 1):

            # 5 - Compare item with next item, if higher, swap and set flag to False, since it's not sorted.
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False


bubble_sort(arr)
print(arr)
