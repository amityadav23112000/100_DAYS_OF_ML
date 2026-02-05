#tuple
# orderd, immutable , allow duplicate values
# tuple are read only data structure

# a= (1,2,3,4,5,1,2)
# print(a)
# print(type(a))
# print(len(a))
# print(a[0])
# print(a[-1])
# print(a[1:4])
# print(a[::-1])
# print(a.count(1))
# print(a.index(4))
# for i in a:
#     print(i)
# a= (1,)
# print(type(a))
# a= ()
# print(type(a))



# set in python 
# unordered , mutable , no duplicate values, indexing and slicing not supported 
# set dnot allow mutable data types like list , dictionary , set as elements

# a= {1,2,3,4,5,1,2}
# print(a)
# print(type(a))
# print(len(a))
# a.add(6)
# print(a)
# a.update([7,8,9])
# print(a)
# a.remove(3)
# print(a)
# # a.remove(10)  # will raise error if element not found
# a.discard(10)   # will not raise error if element not found
# print(a)
# popped_item= a.pop()
# print(popped_item)
# print(a)

#SET FOLLOW HASHING MECHANISM TO STORE ELEMENTS SO THE ORDER OF ELEMENTS MAY VARY EACH TIME YOU RUN THE CODE

# a =set()  
# print(type(a)) set
# A={}
# print(type(A)) dictionary

s1 ={
    1,2,3,4,5
}
s2 ={
    4,5,6,7,8
}
# union
print(s1 | s2)
print(s1.union(s2))
# intersection
print(s1 & s2)
print(s1.intersection(s2))
# difference
print(s1 - s2)
print(s1.difference(s2))
# symmetric difference
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
# subset
print(s1.issubset(s2))
print(s2.issuperset(s1))
# disjoint
print(s1.isdisjoint(s2))  
s3= {6,7}
print(s1.isdisjoint(s3))
# copy
s4= s1.copy()
print(s4)
# clear
s1.clear()
print(s1)
s1.add(10)
print(s1)
s1.update([11,12,13])
print(s1)
# s1.remove(2)
# print(s1)