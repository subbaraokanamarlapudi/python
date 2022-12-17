# Bubble sort

'''
* It is simplest sorting algorithm works repeatdly swapping the adjacent
elements if they are in wrong order.
* This algorithm is not suitable for large data sets as its average and 
worst-case time complexity is quite high.

* Best Time complexity : O(n)
* Average Time comlexity : O(n^2)
* Worst Time complexity : O(n^2)
* Worst case Space complexity : O(1)

'''

# code

def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if(lst[j]>lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]

print("Sorted Elements are:")
lst = [12,43,54,6,789,9]
BubbleSort(lst)
print(lst)