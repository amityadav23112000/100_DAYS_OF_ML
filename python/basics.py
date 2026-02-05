a=[1,2,3]
import sys
print(sys.getsizeof(a))
# print("hello world")
# # print("hello world" , 1, 2, sep="----",end="$$$")
# print("hello"*3)
# # print(type("")== str)
# a= input("enter a string : ")
# b= int(input("enter a integer"))
# c= float(input("enter a float value"))
# print(a,b,c)
# a,b,c=2,3,4
# print(a,b,c)
# a,b,c= c,b,a
# print(a,b,c)

# logical operator = or and not 
# True and False

# __ ="amit"
# print(__)

# type conversion   implicit and explicit
# a= "1111111111111111111111133333333333111111111111111111111111"
# print(int(a)+1)

# a=12333
# print(type(str(a)))
# a=9.5+2
# print(type(a))
# a=9.5+2
# print((int(a)))
#



# literals in python - string , numeric , boolean , special literal - None
# a= None
# print(type(a))

# a= 0b1010
# b= 10
# c= 0o12
# d= 0xA
# print(a,b,c,d)
# print(hex(b))
# print(oct(b))
# print(bin(b))
# print(0b1010,0o12,0xA)

# a= """ hello my name is amit
# i am from delhi
# i love to code
# """
# print(a)

# a= 10+2
# b= 10-3
# c= 10*2
# d= 10/3
# e= 10//3
# f= 10%3
# g= 10**3
# print(a,b,c,d,e,f,g,sep="\n")

# print(2**3**2)  # right to left associativity
# print(1 or 0 and 0)

#  bitwise operator - & | ^ ~ << >>
# a= 10  # 1010
# b= 4   # 0100
# print(a & b)  # 0000 = 0
# print(a | b)  # 1110 = 14
# print(a ^ b)  # 1110 = 14
# print(~a)     # -(a+1) = -11
# print(a << 2) # 101000 = 40
# print(a >> 2) # 0010 = 2


# a++ or a-- # invalid in python
# a=3 
# b=3
# # print(a==b)
# # print(a is b)   is operator checks the memory location
# print(a is not b)

# # print(id(a))
# # print(id(b))

# a= [1,2,3] 
# print(id(a))
# print(1 in a)
# print(4 not in a)



# control flow - if , if else , if elif else
# a= int(input("enter a number : "))
# if a%2==0:
#     print("even")
# else:
#     print("odd")
    
# email = input("enter your email : ")
# password = input("enter your password : ")
# if(email =="yadavamit@gmail.com" and password =="abcd1234"):
#     print("login successful")
# else:
#     print("login failed")
    
    

# loops in python - for , while

# for i in range(1,11):
#     print(i)
#     if i==5:
#         break
# else:
#     print("loop ended normally not with break")
    
# i=1
# while i<=10:
#     print(i)
#     i+=1  
# else:
#     print("loop ended normally not with break")


# for i  in  range(1,6,2):
#     print(i)
#     continue

# for i in range(100,1,-20):
#     print(i)

# i=1
# while i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#         j+=1
#     print("\n")
#     i+=1
    
    
# import random 

# random_number = random.randint(1,100)
# attempts = 0
# max_attempts = 10
# print("Welcome to the Number Guessing Game!")
# while attempts < max_attempts:
#     user_guess = int(input("Enter your guess (between 1 and 100): "))
#     attempts += 1
#     if user_guess < random_number:
#         print("Too low! Try again.")
#     elif user_guess > random_number:
#         print("Too high! Try again.")
#     else:
#         print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
#         break
# else:
#     print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")
    

# for loop work on range and seqeuence such as string , list , tuple , dictionary , set
# for i in "Amit":
#     print(i)

# a= [1,2,3,4,5]
# for i in a:
#     print(i)  

# a= {"name":"amit" , "age":22 , "city":"delhi"}
# for i in a:
#     print(i, ":", a[i])
    
# for i in a.values():
#     print(i)
# for i in a.items():
#     print(i)
# for i in a.keys():
#     print(i)

# a= {1,2,3,4,5}
# for i in a:
#     print(i)

# break , continue , pass
# for i in range(1,11):
#     if i==5:
#         pass
#     print(i)
#     if i==5:
#         break
#     print(i)

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# for i in range(0,6):
#     for j in range(0,i):
#         print("*",end=" ")
#     print("\n")

#  max() , min() , abs() , pow() , round()
# a= -3.7
# print(max(1,2,3,4,5))
# print(min(1,2,3,4,5))     
# print(abs(a))
# print(pow(2,3))
# print(round(a))
# print(round(3.14159,2))
# print(divmod(10,3)[0],divmod(10,3)[1])
# ord() , chr()
# print(ord('a')) print of ascii value
# print(chr(97))   # print of character from ascii value

# import  module
# def helper():
#     print("this is helper function")


# if __name__ == "__main__":
#     helper()
#     print("this is main function")
#     a= module.sum([1,2,3,4,5])
#     print(a)


# import math
# print(math.factorial(5))
# print(math.sqrt(16))
# print(math.gcd(12,15))
# def sum(a):
#     total = 0
#     for i in a:
#         total += i
#     return total
# print(sum([1,2,3,4,5]))
# print(math.pi)

# import random
# print(random.randint(1,100))
# print(random.choice(['apple', 'banana', 'cherry']))
# print(random.shuffle([1, 2, 3, 4, 5]))

# import os
# print(os.getcwd())
# print(os.listdir())
# print(os.path.exists("python/module.py"))
# print(os.path.join("python","module.py"))   
# print(os.path.basename("python/module.py"))
# print(os.path.dirname("python/module.py"))