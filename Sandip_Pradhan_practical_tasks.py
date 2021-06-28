"""1. Create a python program with below mentioned specification.

	- Input the name of the user
	- Input 2 numbers from the user
	- Calculate the following: Addition, Substraction, Multiplication, Division, Factorial
	- Print the output by greeting Hello to the user followed by the results of calculation.
	
	Output Sample:
	
	Hello Deepak, Please find below your calculations.
	Addition: 
	Substraction:
	Multiplication:
	Division:
	Factorial:
	
	Bye, see you next time
	
2. Write a python program to input the temperature of a user in degree celcius and convert it into farenheit.
3. Write a python program to swap the values of 3 variables.
4. Python program to implement below mentioned expressions:
	
		a. Quadratic equation -b + sqrroot(b2-4ac)/2a  -b - sqrroot(b2 - 4ac)/2a
5. Input the values of radius, length and width from a user in a python program and calculate the following:
		a. Area of a circle
		b. Area of a rectangle
		c. Area of a square

"""

import math
print("Hello Sandip")
x=input("enter 1st number:")
y=input("enter 2nd number:")
#1
add=int(x)+int(y)
print("Addition :",add)
dif=int(x)-int(y)
print("Subtraction :",dif)
prd=int(x)*int(y)
print("Multiplication :",prd)
div=int(x)/int(y)
print("Division :",div)

n =int(input("Enter number"))
fact = 1
  
for i in range(1,n+1):
    fact = fact * i
      
print ("The factorial of given number{0} is {1}".format(n,fact))
print (fact)

print ("BYe BYE Bye SEE you next time")

#2


celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

#3
x=input("enter first number:")
y=input("enter second number:")
z=input("enter third number:")
print('value of x is {}'.format(x))
print('value of y is {}'.format(y))
print('value of z is {}'.format(z))
temp_var=x
x=y
y=z
z=temp_var
print('value of x is {}'.format(x))
print('value of y is {}'.format(y))
print('value of z is {}'.format(z))

#4


a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
#under square solution
under = (b**2) - (4*a*c)


negatives_solution = (-b-cmath.sqrt(under))/(2*a)
positive_solution = (-b+cmath.sqrt(under))/(2*a)

print('The Quardaetic equation solution are {0} and {1}'.format(negative_solution,positive_solution))

#5
PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
print(" Area Of a Circle = %.2f" %area)

length= float(input('enter length: '))
width= float(input('enter width: '))
area= length * width
print("Area of Rectangle =%.2f" %area)


length= float(input('enter length: '))
area= length * length
print("Area of Square =%.2f" %area)
