#integer division produces floating point result
#input function gives a string
x=5 
x= x+5
#print(x)

#if else 
x=5 
'''if x>5:
    print("true")
else:
    print("false") '''

x=0.3
x= 3* 5 * (1-x)
#print(x)

#print(5/5) 

a=3
b=50
'''if a > b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is less than {b}")

if a<2:
    print(f"{a} is less than 2")
elif a>2:
    print(f"{a} is greater than 2")
else:
    print("large")

print("all done")

#try except in python
number =input("enter a number")
try:
    newno= int(number)
    print(f"you entered {newno}")
except:
    print("you didn't entered a valid number") '''

def thing():
    print("coding is")
    print("fun")
thing()

def print_lyrics():
    print("hello")
    print("hello I am uzma")


#print_lyrics()

def addtwo(a,b):
    added=a+b
    return added

x=addtwo(3,5)
print(x)
