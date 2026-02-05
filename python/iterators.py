#iterator is an object which implements the __iter__ and __next__ method
#iterable is an object which implements the __iter__ method and returns an iterator
#iterable can be list, tuple, set, dict, string etc
#iterator can be created from iterable using iter() function
#iterator can be used to iterate over the elements of iterable using next() function

#iterators are lazy in nature and do not store all the elements in memory at once
#iterators are used to create generator functions which can generate infinite sequence of values
#iterators are used in for loop to iterate over the elements of iterable

# x= [1,2,3,4,5]
# it= iter(x)
# print(it)  # iterator object
# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3       
# print(next(it))  # 4
# print(next(it))  # 5
# # print(next(it))  # will raise StopIteration error as there are no more elements to iterate
# x= range(1,6)
# it= iter(x)
# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3
# print(next(it))  # 4
# print(next(it))  # 5


# all iterator in python 


def function(it):
    try:
        print(next(it))
        function(it)
    except StopIteration:
        print("end of iterator")
        return


s=[1,2,3,4,5]
function(iter(s))
