'''
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
'''

#Question 5 - Write a program that takes a string input from the user and writes it to a text file. 
str=input("Enter text :")
print(str,file=r"C:\Users\HP\OneDrive\Desktop\Python\textfile.txt")