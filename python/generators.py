#python generator is a special type of iterator that is defined using a function
#generator function uses yield keyword to return values one at a time and maintain its state between successive calls
#when a generator function is called, it returns a generator object without executing the function
#each time next() is called on the generator object, the function executes until it hits a yield statement, which returns the yielded value and pauses the function's state
#the next time next() is called, the function resumes execution right after the yield statement, continuing until it hits the next yield or returns
#generators are memory efficient as they generate values on-the-fly and do not store the entire sequence in memory
#generators are commonly used for iterating over large datasets or infinite sequences   


# def generator_function():
#     for i in range(1,6):
#         yield i
        
# gen= generator_function()
# print(gen)  # generator object
# # print(next(gen))  # 1
# # print(next(gen))  # 2
# # print(next(gen))  # 3
# # print(next(gen))  # 4
# # print(next(gen))  # 5

# for value in gen:
#     print(value)
# print(next(gen))  # will raise StopIteration error as there are no more elements

# genrator expression
gen_exp= (x*x for x in range(1,6))
print(gen_exp)  # generator object
for value in gen_exp:
    print(value)
    

