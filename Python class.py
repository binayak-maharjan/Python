"""print("Hello world","Welcome to python",80 + 20)
print(10 > 5,5 > 10)
x=20
y=3
c=x % y
b='hello'
print(c)
print(type(b))
# x  = int(input("Enter x:"))
# y = int(input("Enter y:"))

print(f'The sum of {x} and {y} is {x+y}')
print(len(b))
c=b.capitalize()
print(c)
print(b.upper())
print(b.strip())
print(b.lower())
print(b.title())
fruit_list=["apple","banana","apple","cherry","cherry"]
print(fruit_list[1])
print(fruit_list[-1])#to view from last
fruit_list.append("orange")#to add new value in list
print(fruit_list)
print(fruit_list[2:5])
fruit_list.remove("banana")
fruit_list.pop(1)
print(fruit_list)
fruit_list.insert(1,"kiwi")
print(fruit_list)
dict = {'name':'Zara','age':7,'class':'First'}
print(dict)
dict['age']=10 #updating existing entry
dict['school']='JEMS' #adding new entry
print(dict)
print(len(dict))
print(dict["age"])
del dict['name']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)
#dict.copy()
#dict.key()
#dict.values()
#dict.items()
print(dict)
student={'name':'Zara','age':7,'class':'First'}
student['name']='Sabin'
print(student)
student['school']='Xaviers'
print(student)
tup=(1,2,3,4,5,6)
print(tup)
print(len(tup))
print(tup[1])
print(tup[-2])
print(tup[3:5])
#tup.append("5") #we cannot add into tuple
thistuple=("apple","banana","cherry")#can be added by converting tuple into list
y=list(thistuple)
y.append("ORANGE")
thistuple=tuple(y)
print(thistuple)
#set
thisset={"apple","banana","cherry","apple"}
print(thisset)
thisset.add("orange")
print(thisset)
#list of dictionary
students=[{'name':'Zara','age':7,'class':'First'},{'name':'Sara','age':9,'class':'First'}]
print(students)
print(students[1])
print(students[0]['age'])
students.append({'name':'Bara','age':8,'class':'First'})
print(students)
#2022-10-18
x=5
y=10
z=3
if(x > y and x> z):
    print(x)
if (y > x and y >z):
    print(y)
if (z > x and z >y):
    print(z)
#username=str(input("Username="))
#password=str(input("Password="))
#if(username == "admin" and password == "admin"):
 #   print("login success")
#else:
 #   print("login failed")
#if else with nested if else
students = [
    {"name": "Dipak", "age": 17, "gender": "male"},
    {"name": "nisma", "age": 15, "gender": "female"},
    {"name": "nishan", "age": 14, "gender": "male"},
    {"name": "swete", "age": 13, "gender": "female"},
]

for student in students:
    if student.get("gender") == "male":
        if student.get("age") >= 15:
            print(student.get("name"), "can vote here")
        else:
            print(student.get("name"), "can not vote here")
    else:
        if student.get("age") >= 14:
            print(student.get("name"), "can vote here")
        else:
            print(student.get("name"), "can not vote here")
#2022-10-19
#for loopsum=0
sum=0
for num in range(0,101):
    sum+=num
print(sum)
#nested loop
for i in range(1, 7):
    for j in range(i):
         print(i, end=' ')
    print()
#infinite loop
while True:
    input_number = int(input("Enter a number or enter 0 to exit: "))
    if input_number == 0:
        print("Existing the program")
        break
    is_prime = True
    for i in range(2, input_number//2 + 1):
        if input_number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Number is PRIME")
    else:
        print("Number is NOT PRIME")
for i in range(11):
    print(i)
    if(i > 5):
        print("before continue")
        break
    print("after continue")
print("finished")
#pattern
for i in range(7,0,-1):
    for k in range(7,i,-1):
        print(end="  ")
    for j in range(i):
        print("*",end=" ")
    print()
#2022-10-20
def student(firstname, lastname='Mark', standard='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')


# 1 keyword argument
student(firstname='John')

# 2 keyword arguments
student(firstname='John', standard='Seventh')
# 2 keyword arguments
student(lastname='Gates', firstname='Bond')

def aver_list(*numbers):
    num=0
    n=0
    for i in numbers:
        num += i
        n = n + 1
    return (num / n)


print(aver_list(1,5,4,7,8,5,2))


def kwargs_example(**person):
    print(type(person))
    for key, value in person.items():
        print(key, "= ", value)

    return person


value = kwargs_example(name="nishma", age=25)


print(value)


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


print(fact(5))
"""
# assignment
# (WAP to sort an array)
a = [2, 4, 3, 7, 1, 9, 5]
temp = 0
print("Elements before sorting:")
for i in range(0, len(a)):
    print(a[i], end=" ")
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i]>a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print()
print("Elements after sorting in ascending order:")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()

# (WAP to sum all the elements in an array.)
a = [2, 4, 3, 7, 1, 9, 5]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
print()
print("The total sum of the elements in an array 'a' =", sum)
print()

# (WAP to count the characters in the string.)
count = 0
word = "Binayak Maharjan"
for i in range(0,len(word)):
    count += 1
print(count)
print()

# (WAP that should take input from the user and it sholud accept input only if the number is between 0 and 100.)
num = int(input("Enter number:"))
while num < 0 or num > 100:
    again = int(input("Please enter again:"))
    num = again
print("Your number is:", num)
print()

# WAP to find the first prime number in an array.
array = [4, 8, 5, 6, 7, 9, 10]
i = 0
for i in range(0, len(array)):
    for j in range(2, int(array[i]/2)+1):
        if array[i] % j == 0:
            break
    else:
        print(array[i], "is a first prime number.")
        break
print()

# WAP to find the sum of digits of a number.
num = 454
num1 = num % 10
num2 = int(num / 10)
num3 = num2 % 10
num4 = int(num2 / 10)
total = num1 + num3 + num4
print("Input number:", num)
print("Output:", total, "which is the sum of", num1, "+", num3, "+", num4)
print()

# Print inverted hash pattern
for i in range(5, 0, -1):
    for k in range(5, i, -1):
        print(end="")
    for j in range(i):
        print("#", end=" ")
    print()
print()

# WAP to reverse a string without using the string function.


def reverse(a):
    rev = ""
    for i in a:
        rev = i + rev
    return rev


string = "ReversE"
print("The original text is:", string)
print("The text after reversing is:", reverse(string))
print()

# WAP to swap two numbers without using a third variable.
a = 10
b = 20
print("Before swapping: a=", a, "and b=", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a=", a, "and b=", b)
print()

# WAP to count the number of words in a string.
str = "Hello it is Python"
count = 1
for i in range(len(str)):
    if str[i] == " " or str == "\n" or str == "\t":
        count = count + 1
print("Total words in the sentence", "'",  str, "'",  "is:", count, "\n")

# WAP to find whether the number is prime or not.
num = 100
for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        print(num, "is not a prime number.")
        break
else:
    print(num, "is a first prime number.")
print()

# WAP to find the largest and smallest element in an array.
arr = [90, 4, 0, 7, 40, 2, 34]
temp = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]>arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("The largest element is:", arr[-1])
print("The smallest element is: ", arr[0])
print()

# WAP to print true if x followed by x otherwise false.


def check(a):
    for i in a:
        if "xx" in a:
            return "true"
        return "false"


print(check("axaxbb"))
