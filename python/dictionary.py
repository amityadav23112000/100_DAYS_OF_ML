#dictionary  has key value pair
#dictionary is mutable
#keys are unique and immutable
#values are mutable and allow duplicate values 

#mutable data types like list , dictionary , set can be used as values but not as keys
#immutable data types like string , tuple , int , float , bool can be used as keys


# d={}
# print(type(d))  #dictionary
# d2= dict()
# print(type(d2))  #dictionary
# d3= {1:"amit" , 2:"yadav" , 3:"kumar"}
# print(d3)
# print(len(d3))
# print(d3[1])
# d3[4]= "new value"
# print(d3)
# d3[2]= "updated value"
# print(d3)

# # d3[ [5,6] ]= "list as key"  # will raise error
# # print(d3)
# d3[ (5,6) ]= "tuple as key"
# print(d3)
# d3[ "name" ]= ["amit" , "yadav"]
# print(d3)
# print(d3.keys())
# print(d3.values())
# print(d3.items())


d1 ={1:"amit" , 2:"yadav" , 3:"kumar"}

# for x,y in d1.items():
#     print(x, ":", y)

# if 2 in d1:
#     print("key 2 is present in dictionary")
# else:
#     print("key 2 is not present in dictionary")

# d1.pop(2)
# print(d1)

# d1.popitem()
# print(d1)


# print(d1.get(3))  #value of key 3
# print(d1.get(4,"key not found"))  #value of key 4
# d1.clear()
# print(d1)   
# # del d1
# # print(d1)  # will raise error as d1 is deleted
# # d2= d1.copy()

# # print(d2)
# # d3= dict.fromkeys( ["a","b","c"] , 0)
# # print(d3)
# l1= [1,2,3]
# l2 = ["amit" , "yadav" , "kumar"]
# d4= dict( zip(l1,l2) )
# print(d4)

# d1={1:"amit" , 6:"yadav" , 3:"kumar"}
# d2={3:"singh" , 4:"new"}
# d1.update(d2)
# print(d1)

# # x= d1+d2  # will raise error
# #print(x)
# x= {k:v for k,v in d1.items()}
# print(x)
# x= {**d1 , **d2}
# print(x)

# for key in sorted(d1):
#     print(key, ":", d1[key])

# print(sorted(d1))
# print(len(d1))
# print(min(d1))
# print(max(d1))
# print(sum(d1))
# print(dict(sorted(d1.items())))

# print(dict(reversed(list(d1.items()))))