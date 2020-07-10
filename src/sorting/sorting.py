# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    left, right = 0, 0

    while right < len(arrA) and left < len(arrB):
        if arrA[right] < arrB[left]:
            merged_arr.append(arrA[right])
            right += 1
        else:
            merged_arr.append(arrB[left])
            left += 1
        
    if right == len(arrA): 
        merged_arr.extend(arrB[left])
    else: 
        merged_arr.extend(arrA[right])
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

