# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    arrA_index = 0
    arrB_index = 0
    merged_index = 0

    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[merged_index] = arrA[arrA_index]
            merged_index += 1
            arrA_index += 1
        else: 
            merged_arr[merged_index] = arrB[arrB_index]
            merged_index += 1
            arrB_index += 1
        
    while arrA_index < len(arrA):
        merged_arr[merged_index] = arrA[arrA_index]
        merged_index += 1
        arrA_index += 1
    while arrB_index < len(arrB):
        merged_arr[merged_index] = arrB[arrB_index]
        merged_index += 1
        arrB_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_side = merge_sort(left)
        right_side = merge_sort(right)

        arr = merge(left_side, right_side)

    return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

