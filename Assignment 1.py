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

