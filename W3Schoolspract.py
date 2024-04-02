#String slicing
'''b=" hello, world!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(len(b))
print(b[-5:-2])
print(b.upper())
print(b.lower())
print(b.strip()) #removes spaces from start and end
print(b.replace("o,","ee"))
print(b.split(","))'''
#string concatenation
a= "hello"
b= "world"
c= a+" " +b
#print(c)
#format strings
age=30
txt="My name is uzma I am {} year old"
#print(txt.format(age))
age=40
#print(f"My name is uzma I am {age} years old") 

name="uzma"
age=50
schoolName= "ALS"
#print(f"My name is {name}. I am {age} years old. I did my matric from {schoolName}")

txt="hello my name is \n \"uzma\"  "
print(txt)

#LIST
mylist = ["apple","onion","garlic"]
#print(mylist)
list1 = [1,3,4,5]
#print(list1)
list2=["uzma",1,4.5]
#print(list2)
#print(type(list2))

thisislist = list(("apple","banana","onion","orange"))
#print(thisislist)
#print(thisislist[0])
#print(thisislist[-1])
#print(thisislist[2:5])
#print(thisislist[:4])
if "apple" in thisislist:
    print("yes")

thisislist[1]="apple"
#print(thisislist)

thisislist[1:3]=["aple","aple","aple"]
#print(thisislist)
thisislist.insert(2,"watermelon")
#print(thisislist)

thisislist=["apple","banana","cherry"]
thisislist.append("orange")
print(thisislist)
thisislist.insert(1,"I am inserted at index 1")
print(thisislist)
thisislist.remove("banana")
print(thisislist)
