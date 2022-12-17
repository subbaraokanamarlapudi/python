# Heap sort
# Heapsort is a popular and efficient sorting algorithm. 
# The concept of heap sort is to eliminate the elements one by one from the heap part of the list, and then insert them into the sorted part of the list.
'''
* It is a process of creating the min-heap or max-heap using
the elements of the given array.
* Min-heap or Max-heap represents the ordering of array in which
roots element represents the minimum or maximum array.

* Heap sort basically performs two operations:
  1.Build a heap H, using the elements of array.
  2.Repeatedly delete the root element of the heap formed in 1st phase.

* Best Time complexity : O(n logn)
* Average Time comlexity : O(n logn)
* Worst Time complexity : O(n logn)
* Worst case Space complexity : O(1)
'''

# code

from heapq import heappop, heappush  
   
def heapsort(list1):  
     heap = []  
     for ele in list1:  
         heappush(heap, ele)  
   
     sort = []  
    
     while heap:  
         sort.append(heappop(heap))  
   
     return sort  
   
list1 = [27, 21, 55, 15, 60, 4, 11, 17, 2, 87]  
print(heapsort(list1))