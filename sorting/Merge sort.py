# Merge sort
# It follows the Divide and conquer rule.
'''
* It is similar to Quick sort algorithm and it works on divide and conquer rule.
* It divides the given list into 2 halves i.e sublist.
* That sublist is divided again and again into 2 halves untill,we get one element each.
* We combine to pair of one element list into 2 element lists.
The sortes 2 elements pair is merged into 4 elements list and so on... untill the sorted list.
* It can implement 2 ways:
  1.Top-down approach.
  2.Bottom-up approach

* Best Time complexity : O(n logn)
* Average Time comlexity : O(n logn)
* Worst Time complexity : O(n logn)
* Worst case Space complexity : O(n)
'''

# code

def merge_sort(lst):
    if len(lst) <= 1:
        return

    mid = len(lst)//2

    left = lst[:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    
    merge_two_sorted_lists(left, right, lst)
    
def merge_two_sorted_lists(a,b,lst):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            lst[k] = a[i]
            i+=1
        else:
            lst[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        lst[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        lst[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [],
        [3],
        [9, 8, 7, 2],
        [3, 4, 1, 2, 5],
        [6, 5, 12, 10, 9, 1],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [10, 3, 15, 7, 8, 23, 98, 29]
    ]

    for lst in test_cases:
        print("Before : ",lst,end="  ->  ")
        merge_sort(lst)
        print("After : ",lst)

 