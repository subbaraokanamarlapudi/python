# Insertion sort

'''
* It is simple algorithm. It is straight forward and more efficient
than they have have previous Bubble sort algorithm.
* It is a concept of deck of cards,where we sort the playing card according
to particular card.

* Best Time complexity : O(n)
* Average Time comlexity : O(n^2)
* Worst Time complexity : O(n^2)
* Worst case Space complexity : O(1)
'''
# code

def InsertionSort(lst):
    n = len(lst)
    for i in range(1,n): 
        for j in range(i-1,-1,-1):  
            if(lst[j]>lst[j+1]):
                lst[j],lst[j + 1] = lst[j + 1],lst[j]
            else:
                break

print("Sorted Elements are: ")
lst = [12,43,54,6,789,9]
InsertionSort(lst)
print(lst)