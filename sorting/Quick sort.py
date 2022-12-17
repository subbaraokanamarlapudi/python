# Quic k sort

'''
* Like Merge sort, Quick sort also follows Divide and conquer rule.
* It picks an element as a pivot and partitions the given array
around the picked pivot.
* There are many different versions of quick sort:
  1.Always pick the first element as a pivot.
  2.Always pick the last element as a pivot.
  3.Pick a random element as a pivot.
  4.Pick median as the pivot.

* Best Time complexity : O(n logn)
* Average Time comlexity : O(n logn)
* Worst Time complexity : O(n^2)
* Worst case Space complexity : O(n)
'''

# code

def partition(lst,l,r):
    pi = lst[r]
    j = l
    for i in range(l,r):
        if(lst[i]<=pi):
            lst[i],lst[j] = lst[j],lst[i]
            j+=1
    lst[j],lst[r] = lst[r],lst[j]

    return j

def quick_sort(lst,l,r):
    if(l<r):
        pi = partition(lst,l,r)

        quick_sort(lst,l,pi-1)
        quick_sort(lst,pi+1,r)
    return lst

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
        print("Before : ",lst,end=" ")
        print(" -> ","After : ", quick_sort(lst,0,len(lst)-1))