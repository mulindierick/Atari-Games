# a tree but left and right is less than head. left and right have no relationship
# heapify - extra min, which is the top.. get the last element, make it the root and then move down until it is in place
#  heap as an array - left child = 2i + 1, right 2i + 2, root/parent = (i-1)//2
# build heap - o(n)
# heapify - o(logn)
# extra min - o(nlogn)