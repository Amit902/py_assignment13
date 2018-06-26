#Q1. Name and handle the exception occured in the following program:
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)     #ZeroDivisonErrror occured here snd it can be handled by exception class
except Exception:
        print("An Exception occured")


#Q.2- Name and handle the exception occurred in the following program:
try:
    l=[1,2,3]
    print(l[3])   #indexErrorand list is out of range
except Exception:
    print("The list is out of range")


#Q.3 - What will be the output of the following code:

#Program to depict Raising Exception

# try:
#     raise NameError("H
# #output
# An exception
#     raise NameError("Hi there")  # Raise Error
# NameError: Hi there


#Q.4- What will be the output of the following code:

# Function which returns a/b
# def AbyB(a , b):i there")  # Raise Error
# except NameError:
#     print("An exception")
#     raise  # To determine whether the exception was raised or not
#
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print ("a/b result in 0")
# 	else:
# 		print(c)
#
# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

#Output
# -5.0
# a/b result in 0


#Q.5- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error
#import Error
try:
    import abcd
    import amit.abcd

except Exception as exception:
    print(exception)


#value Error
try:
    number=int("hii python")

except ValueError  as f:
    print(f)


#Index Error
try:
    l=[1,2,3,4,5]
    print(l[5])
except Exception as e:
     print(e)

#In this program indexError will occured and list is out of range i.e index error.


#Q.6- Create a user-defined exception AgeTooSmallError() that
# warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).
class AgeTooSamllError(Exception):
    pass

age=0

while age<18:
    age=int(input("Enter your age: "))
    try:
        if age<18:
            raise AgeTooSamllError("age too small")

    except Exception as e:
        print(e)
