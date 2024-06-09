#Question 1 - Write a program that takes two numbers as input and prints their sum. 
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
sum=a+b
print("Sum of the two numbers :",sum)

#Question 2 - Write a python program that checks whether a given number is even or odd.
num=int(input("Enter a number :"))
if num%2==0:
    print("The given number is even")
else:
    print("The given number is odd")

#Question 3 - Write a python program that calculates the factorial of a given number. 
n=int(input("Enter a number :"))
fact=1
for i in range (2,n+1) :
    fact=fact*i
print("The factorial of the given number :",fact)

#Question 4 - Write a program that asks the user for their name and then prints a greeting message. 
name=input("Enter your name :")
print("Hello {}, Welcome to our session".format(name))

#Question 5 - Write a program that takes a string input from the user and writes it to a text file. 
samplefile=open("textfile.txt","w")
str=input("Enter your string :")
print(str,file=samplefile)

#Question 6 - Write a program that reads the content of a text file and prints it to the console. 
samplefile=open("textfile.txt","r")
print(samplefile.read())

#Question 7 - Write a python program that takes a string as input and returns its length. 
str=input("Enter your string :")
print("Length of given string is :",len(str))

#Question 8 - Write a python program that concatenates two strings and returns the result.
str1=input("Enter first string :")
str2=input("Enter second string :")
print("Concatenated string is :",str1+str2)

#Question 9 - Write a python program that checks if a substring is present in a given string. 
str=input("Enter string :")
substr=input("Enter substring :")
print(substr in str)

#Question 10 - Write a python program that converts a given string to uppercase. 
str=input("Enter string :")
print(str.upper())

#Question 11 - Write a python program that generates the first n numbers in the Fibonacci sequence. 
n=int(input("Enter number of terms :"))
a=1
b=1
c=a+b
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

#Question 12 - Write a python program that calculates the sum of the digits of a given number. 
num=int(input("Enter number :"))
sum=0
while num>0 :
    digit=num%10
    sum+=digit
    num//=10
print("Sum of digits of the given number :",sum)

#Question 13 - Write a program that asks the user for their birth year and calculates their age. 
year=int(input("Enter year of birth :"))
age=2024-year
print("Age :",age)

#Question 14 - Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines=[]
while True:
    line=input("Enter a line of input :")
    if line=='':
        break
    lines.append(line)
for line in lines :
    print(line)

#Question 15 - Write a program that reads data from a CSV file and prints it to the console. 
import csv 
samplefile=open("samplefile.csv","w")
samplefile.write("Hello my name is Sommya Jain.\n")
samplefile.close()
samplefile=open("samplefile.csv","r")
print(samplefile.read())
samplefile.close()

#Question 16 - Write a program in python that counts the frequency of each character in a string. 
dic={}
str=input("Enter a string :")
for i in str :
    if i in dic :
        dic[i]+=1
    else :
        dic[i]=1
print(dic)

#Question 17 - Write a program in python that converts a given string to title case (first letter of each word capitalized). 
str=input("Enter a string :")
print(str.title())

#Question 18 - Write a python program that checks if two strings are anagrams of each other.
str1=input("Enter first string :")
str2=input("Enter second string :")
if sorted(str1)==sorted(str2):
    print("Strings are anagrams")
else :
    print("Strings are not anagrams")

#Question 19 - Write a python program that checks if a given string is a palindrome.
str=input("Enter a string :")
for i in str :
    if i.isalnum():
        print(i,end="")

#Question 20 - Write a python program that takes a list of numbers and returns their sum. 
l=eval(input("Enter a list of numbers :"))
sum=0
for i in l:
    sum+=i
print(sum)

#Question 21 - Write a python program that counts the occurrences of a specific element in a list. 
l=eval(input("Enter a list of numbers :"))
e=int(input("Enter the element you want to count :"))
count=0
for i in l :
    if i==e :
        count+=1
print(count)

#Question 22 - Write a python program that returns the minimum and maximum values in a list of numbers. 
l=eval(input("Enter a list of numbers :"))
print("Minimum value :",min(l))
print("Maximum value :",max(l))

#Question 23 - Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 
scale=input("Choose Celsius(C) or Fahrenheit(F) :")
if (scale=='C') :
    temp=float(input("Enter temperature in Celsius :"))
    print("Temperature in Fahrenheit :",(temp*9/5)+32)
else :
    temp=float(input("Enter temperature in Fahrenheit :"))
    print("Temperature in Celsius :",(temp-32)*5/9)

#Question 24 - Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
a=float(input("Enter first number :"))
op=input("Enter operator (+, -, *, /) :")
b=float(input("Enter second number :"))
if (op=='+') :
    print(a+b)
elif (op=='-') :
    print(a-b)
elif(op=='*') :
    print(a*b)
elif (op=='/') :
    if (b==0) :
        print("Cannot divide by 0")
    else :
        print(a/b) 
else :
    print("Invalid operator")

#Question 25 - Write a program that copies the contents of one text file to another. 
file1 = open("file1.txt",'w')
file1.write("Hello everyone! This is the text to be copied")
file1.close()
file2=open("file2.txt",'w')
file1=open("file1.txt","r")
file2.write(file1.read())
file1.close()
file2.close()

#Question 26 - Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
str=input("Enter a string:")
prefix=input("Enter a prefix :")
suffix=input("Enter a suffix :")
print(str.startswith(prefix) or str.endswith(suffix))

#Question 27 - Write a program in python that converts a string into a list of its characters. 
str=input("Enter a string:")
lst=[]
for i in str:
    lst.append(i)
print(lst)
