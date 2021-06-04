#Lists
# x is the variable name
#To write the list we open square brackets and then insert values seperated by commas.
#To store strings we write it in double quotes/single
#x = ["abc","def","ghi"]
#Access values using index ----> list_name[index]
#print(x)
#v = 0
#print(x[v])
#print(x[1])

#Changing the value at particular index
#x[0] = "jkl"

#Appending a new value inside the list ----> list_name.append(Value to be added)
#x.append(2)
#x.append("Three")

#Adding values at particular index inside the list ---> list_name.insert(index,value)
#x.insert(1,"Added")

#Removing known values from the list ---> list_name.remove(value)
#x.remove("def")

#Removing value at a particular index
#x.pop(1)
#x.pop()              -> it will remove the last element of the list

#Get length of the list ----> len(list_name)
#l = len(x)
#print(l)















#Dictionary
#d = {'key1':"value1","key2":"value2","key3":"value3"}

#Access values in dict ---> dict_name["key_name"]
#key1 = "key1"
#print(d["key1"])

#Access using the get method ---> dict_name.get("key")
#print(d.get('key3'))


#Get length of dict using len(dict_name)
#print(len(d))

#Changing values inside dict ---> dict_name['key'] = new_value
#d['key2'] = 500

#Adding a new value to the dict.
#d['key4'] = ["Newly Added"]

#Removing elements from the dict
#d.pop('key1')
#print(d)








#Dont use space to ident your code, use tab

#If elif else
"""
a = 30
b = 30
if a < b:
    print("b is greater")
elif a == b:
    print("Equal")
else:
    print("a is greater")

print("Done")
"""


#For Loops

"""
for i in range(0,6):
    print(i)

x = "Ravi"
for i in x:
    print(i,end="")


x = [1,2,3,3]
for i in x:
        print(i)

x = [1,2,3,3]
for i in range(0,len(x)):
    x[i] = 1
    print(x)
"""



#Functions

"""
def function_name():
    #Block of Code
    print("Hello World")

#Call the function
function_name()


#You might have to execute some block of codes multiple times with different values.
def func_with_para(a,b):
    print(a)
    print(b)

func_with_para(20,"Para2")
func_with_para(40,"Parafghvc")



#Functions returning values
def func_return(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

s1,s2 = func_return(20,40)
print(s1)
print(s2)
"""

"""
#How to take input from user -----> input("Message")
#input returns a str

i = input("Enter Number 1")
j = int(i)
print(type(i))
"""


#How to create class
"""
class Student():
    name = "Ravi"
    usn = "1by18cdqw"
    def study():
        print("He is studing")

s1 = Student() #how you create object of class. This is same as telling "S1 you are a student"
print(s1.usn) #To access the features of the class we will have to use . operator (object.featutre)
s1.study()


class Student():
    def __init__(self,name,usn):
        self.name = name
        self.usn = usn
    def study(self,sub):
        print(self.name)
        print("I am studing " + sub )

s1 = Student("Sathvik","1by1cxaskcsd")
s2 = Student("Roshni","1by1ikuchasdx")
print(s1.name + s1.usn)
print(s2.name + s2.usn)
s1.study("Web dev")


try:
    a = 5
except Exception as e:
    print("There is some error in try block")
else:
    print("Will execute only if there is no error inside the try block")
finally:
    print("Will execute irrespective of the error")
"""
