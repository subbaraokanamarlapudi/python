#Selection sort

'''
* It sorts an array by repeadtly finding the minimm elememt from unsoretd array and keep it at beginning.
* The algorith maintains 2 subarrays:
   1. Subarray which is already sorted.
   2. Remaining subarray which is unsorted.
* Best Time complexity : O(n^2)
* Average Time comlexity : O(n^2)
* Worst Time complexity : O(n^2)
* Worst case Space complexity : O(1)
'''

#code

def SelectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if(lst[j]<lst[min_idx]):
                min_idx = j
        lst[i],lst[min_idx] = lst[min_idx],lst[i]

print("Sorted Elements are:")
lst = [12,23,24,51,1,3]
SelectionSort(lst)
print(lst)