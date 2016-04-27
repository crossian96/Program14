from modCustomSet import *


a1=CustomSet([1,1,2,3,4,4,5]) #Method 1: Constructing Object
print(a1)

print(CustomSet.brackets(a1)) #Method 9

6 in a1           #Method 5
4 in a1


#testing program 6,7,8
x = [1,2,3]
y = [1,2,3,4,4]
a=CustomSet(x)
b=CustomSet(y)
print("Testing 6, 7 and 8")
print("a>=b ",a>=b)
print("a<=b ",a<=b)
print("length b ",len(b))
