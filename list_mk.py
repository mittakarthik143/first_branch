import os

list1 = [0,9,3,6,1,10]
list1.reverse()
print('The reversed list is', list1)

list2=[91,67,120,34,76,54,78,87,64,345]
list2.sort()
print('The sorted list is', list2)

list3=[]
print(dir(list1))
list3=list1[::]
print('List3 is - ', list3)
indexvalue = list2[2:6]
print('The index values are', indexvalue)
